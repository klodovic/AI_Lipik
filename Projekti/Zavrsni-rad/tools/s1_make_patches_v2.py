import os
import numpy as np
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from pathlib import Path
import logging

# --- KONFIGURACIJA ---
BASE_DIR = Path("D:/copernicus-zagreb")
RAW_DIR = BASE_DIR / "data/raw/sentinel2"
AOI_PATH = BASE_DIR / "data/reference/aoi_zagreb.geojson"
OUT_DIR = BASE_DIR / "data/patches_c4"
PATCH_SIZE = 64
STRIDE = 48  # Pomak (48 daje preklapanje, 64 ne daje)

OUT_DIR.mkdir(parents=True, exist_ok=True)

# --- LOGIRANJE (UTF-8 fiks) ---
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
log_file = BASE_DIR / "patching.log"

file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(log_formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# --- UCITAVANJE AOI ---
try:
    aoi = gpd.read_file(AOI_PATH)
    logging.info(f"Učitan AOI: {AOI_PATH.name}")
except Exception as e:
    logging.error(f"Greška pri učitavanju AOI: {e}")
    exit()

def get_sentinel_paths(tile_dir):
    paths = {}
    for f in tile_dir.glob("*.jp2"):
        if "B04_10m" in f.name: paths['B04'] = f
        if "B08_10m" in f.name: paths['B08'] = f
        if "B11_20m" in f.name: paths['B11'] = f
    return paths

def process_tiles():
    years = sorted([d for d in RAW_DIR.iterdir() if d.is_dir()])
    total_patches = 0
    
    for year_dir in years:
        year = year_dir.name
        tiles = [d for d in year_dir.iterdir() if d.is_dir()]
        
        for tile_dir in tiles:
            tile_name = tile_dir.name
            logging.info(f"Obrada: {year} | {tile_name}")
            
            paths = get_sentinel_paths(tile_dir)
            if len(paths) < 3:
                logging.warning(f"Preskačem {tile_name}: Nedostaju kanali.")
                continue

            try:
                with rasterio.open(paths['B04']) as src_b4, \
                     rasterio.open(paths['B08']) as src_b8, \
                     rasterio.open(paths['B11']) as src_b11:
                    
                    aoi_projected = aoi.to_crs(src_b4.crs)
                    
                    # Maskiranje i rezanje na granice Zagreba
                    out_img_b4, _ = mask(src_b4, aoi_projected.geometry, crop=True)
                    out_img_b8, _ = mask(src_b8, aoi_projected.geometry, crop=True)
                    out_img_b11, _ = mask(src_b11, aoi_projected.geometry, crop=True)
                    
                    # Upsample B11 (20m -> 10m) da odgovara B04/B08
                    out_img_b11 = np.repeat(np.repeat(out_img_b11, 2, axis=1), 2, axis=2)
                    out_img_b11 = out_img_b11[:, :out_img_b4.shape[1], :out_img_b4.shape[2]]

                    # Izračun NDVI (Vegetacijski indeks)
                    red = out_img_b4[0].astype(float)
                    nir = out_img_b8[0].astype(float)
                    denom = nir + red
                    ndvi = np.divide(nir - red, denom, out=np.zeros_like(nir), where=denom!=0)
                    
                    # Stack: [NDVI, B04, B08, B11]
                    stacked = np.stack([ndvi, red, nir, out_img_b11[0]])
                    
                    _, h, w = stacked.shape
                    tile_patch_count = 0
                    
                    # Dvostruka petlja za rezanje (sa STRIDE pomakom)
                    for y in range(0, h - PATCH_SIZE, STRIDE):
                        for x in range(0, w - PATCH_SIZE, STRIDE):
                            patch = stacked[:, y:y+PATCH_SIZE, x:x+PATCH_SIZE]
                            
                            # Provjera: Ako je B04 (red) kanal prazan (0), patch je izvan Zagreba
                            if np.mean(patch[1]) < 1: 
                                continue
                                
                            patch_name = f"{year}_{tile_name}_y{y}_x{x}.npz"
                            
                            # BRŽE SPREMANJE (bez kompresije za brzinu, .npz format)
                            np.savez(OUT_DIR / patch_name, x=patch.astype(np.float32))
                            tile_patch_count += 1
                    
                    logging.info(f"Završeno {tile_name} | Generirano: {tile_patch_count} patcheva")
                    total_patches += tile_patch_count

            except ValueError:
                logging.info(f"Tile {tile_name} se ne preklapa s AOI (preskačem).")
            except Exception as e:
                logging.error(f"Greška na {tile_name}: {e}")

    logging.info(f"--- GOTOVO --- Ukupno patcheva na disku: {total_patches}")

if __name__ == "__main__":
    process_tiles()