import sys
from pathlib import Path
import torch
import torch.nn as nn
import numpy as np
import json
import re
import shutil
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFilter

# --- KONFIGURACIJA ---
BASE_DIR = Path("D:/copernicus-zagreb")
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from models.model_v2 import MasterUNet

PATCH_DIR = BASE_DIR / "data/patches_c4"
MODEL_PATH = BASE_DIR / "model_v3/master_model_v3_final.pth"
GEOJSON_PATH = BASE_DIR / "data/reference/aoi_zagreb.geojson"
OUTPUT_DIR = BASE_DIR / "data/projections_v3"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

META_SOURCE = BASE_DIR / "data/projections/metadata_full_2027.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def apply_city_mask(image, bounds):
    if not GEOJSON_PATH.exists(): return image
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    try:
        with open(GEOJSON_PATH, "r") as f: geo = json.load(f)
        for feat in geo['features']:
            geom = feat['geometry']
            polys = geom['coordinates'] if geom['type'] == 'Polygon' else [p for sub in geom['coordinates'] for p in sub]
            for poly in polys:
                px = [((c[0] - bounds[0][1]) / (bounds[1][1] - bounds[0][1]) * image.size[0],
                       (1 - (c[1] - bounds[0][0]) / (bounds[1][0] - bounds[0][0])) * image.size[1]) for c in (poly[0] if isinstance(poly[0][0], list) else poly)]
                if len(px) > 2: draw.polygon(px, fill=255)
    except: return image
    img_np = np.array(image)
    mask_np = np.array(mask)
    if img_np.shape[2] == 4:
        img_np[:, :, 3] = np.where(mask_np == 0, 0, img_np[:, :, 3])
    return Image.fromarray(img_np)

def run_v5_erosion_processing():
    print("\n--- GENERIRANJE EROZIJE VEGETACIJE ---")
    
    target_meta = OUTPUT_DIR / "metadata_full_2027.json"
    if not target_meta.exists() and META_SOURCE.exists():
        shutil.copy(META_SOURCE, target_meta)
    with open(target_meta, "r") as f: meta = json.load(f)
    bounds = meta['bounds']

    model = MasterUNet().to(DEVICE)
    if hasattr(model, 'final'): model.final[0] = nn.Conv2d(32, 1, kernel_size=1).to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.eval()

    all_files = list(PATCH_DIR.glob("*.npz"))
    max_y, max_x = 0, 0
    valid_files = []
    for f in all_files:
        match = re.search(r'_y(\d+)_x(\d+)', f.name)
        if match:
            y, x = int(match.group(1)), int(match.group(2))
            max_y, max_x = max(max_y, y), max(max_x, x)
            valid_files.append((f, y, x))

    canvas_2016 = np.zeros((max_y + 64, max_x + 64))
    canvas_2027 = np.zeros((max_y + 64, max_x + 64))
    counts = np.zeros((max_y + 64, max_x + 64))

    for f_path, y, x in tqdm(valid_files, desc="🛰️ Analiza"):
        with np.load(f_path) as loader: raw_data = loader['x']
        canvas_2016[y:y+64, x:x+64] += raw_data[0]
        sample = torch.from_numpy(raw_data).float().to(DEVICE).unsqueeze(0).unsqueeze(0).repeat(1, 5, 1, 1, 1)
        sample[:, :, 1:] /= 10000.0
        with torch.no_grad():
            pred = model(sample)
            res = pred[0, 0, 0].cpu().numpy() if len(pred.shape) == 5 else pred[0, 0].cpu().numpy()
            canvas_2027[y:y+64, x:x+64] += res
        counts[y:y+64, x:x+64] += 1

    f16 = np.divide(canvas_2016, counts, out=np.zeros_like(canvas_2016), where=counts!=0)
    f27 = np.divide(canvas_2027, counts, out=np.zeros_like(canvas_2027), where=counts!=0)
    delta_total = f16 - f27
    delta_total = np.maximum(delta_total, 0)

    for yr in range(2026, 2052, 2):
        progress = (yr - 2026) / 24.0
        current_ndvi = f16 - (delta_total * progress)
        
        # DINAMIČKI PRAG: 2026 (0.22) -> 2050 (0.35)
        # Što je veći progres, to više zelenila proglašavamo 'mrtvim' (sivim)
        dynamic_threshold = 0.22 + (progress * 0.13)
        
        h, w = current_ndvi.shape
        rgb = np.zeros((h, w, 4), dtype=np.uint8)
        
        concrete = current_ndvi < 0.12
        urban = (current_ndvi >= 0.12) & (current_ndvi < dynamic_threshold)
        forest = current_ndvi >= dynamic_threshold
        
        rgb[concrete, 0:3] = [55, 55, 60]      # Beton
        rgb[urban, 0:3] = [135, 135, 130]    # Urbano/Suho
        
        # Intenzivno zelena za preostalu šumu
        g_val = ((current_ndvi[forest] - dynamic_threshold) / (0.8 - dynamic_threshold) * 100 + 70).astype(np.uint8)
        rgb[forest, 0], rgb[forest, 1], rgb[forest, 2] = 30, g_val, 30
        rgb[..., 3] = 255
        
        img = apply_city_mask(Image.fromarray(rgb), bounds)
        img.save(OUTPUT_DIR / f"ndvi_{yr}.png")
        
        # Heatmap
        if yr > 2026:
            p_val = 100 - (progress * 4.5)
            thresh = np.percentile(delta_total, p_val)
            mask_np = np.where(delta_total > thresh, 255, 0).astype(np.uint8)
            img_mask = Image.fromarray(mask_np).filter(ImageFilter.MaxFilter(7))
            heat = Image.new("RGBA", img_mask.size, (255, 0, 150, 200))
            final_h = Image.new("RGBA", img_mask.size, (0,0,0,0))
            final_h.paste(heat, (0,0), mask=img_mask)
            apply_city_mask(final_h.filter(ImageFilter.GaussianBlur(1.5)), bounds).save(OUTPUT_DIR / f"heatmap_{yr}.png")

    print("✅ Sve mape su generirane.")

if __name__ == "__main__":
    run_v5_erosion_processing()