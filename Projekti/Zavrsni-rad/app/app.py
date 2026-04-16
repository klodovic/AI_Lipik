import streamlit as st
import folium
from streamlit_folium import folium_static
import json
import base64
from pathlib import Path

# --- KONFIGURACIJA ---
BASE_DIR = Path("D:/copernicus-zagreb")
PROJECTION_DIR = BASE_DIR / "data/projections_v3"
GEOJSON_PATH = BASE_DIR / "data/reference/aoi_zagreb.geojson"
META_PATH = PROJECTION_DIR / "metadata_full_2027.json"

st.set_page_config(page_title="Zagreb 2050 AI Vision", layout="wide")

def get_base64_img(path):
    if not path.exists(): return None
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"

# --- SIDEBAR ---
st.sidebar.title("Kontrole simulacije")
viz_mode = st.sidebar.radio(
    "Način prikaza:", 
    ["Simulacija Vegetacije (NDVI)", "🚧 Nova gradilišta (Heatmap)"]
)

year = st.sidebar.slider("Odaberi godinu:", 2026, 2050, 2026, step=2)
opacity = st.sidebar.slider("Prozirnost AI sloja:", 0.0, 1.0, 0.9)

# --- GLAVNI PRIKAZ ---
st.title("Zagreb 2050: Dinamička Projekcija Urbanizacije")

if META_PATH.exists():
    with open(META_PATH, "r") as f: meta = json.load(f)
    bounds = meta['bounds']
    col_map, col_stats = st.columns([3, 1])

    with col_map:
        m = folium.Map(location=[45.815, 15.981], zoom_start=11, tiles="cartodbpositron")
        
        if "Vegetacije" in viz_mode:
            img_path = PROJECTION_DIR / f"ndvi_{year}.png"
            data = get_base64_img(img_path)
            if data:
                folium.raster_layers.ImageOverlay(data, bounds=bounds, opacity=opacity).add_to(m)
        else:
            # Heatmap Mode
            base = get_base64_img(PROJECTION_DIR / "ndvi_2026.png")
            if base: folium.raster_layers.ImageOverlay(base, bounds=bounds, opacity=0.4).add_to(m)
            
            heat_path = PROJECTION_DIR / f"heatmap_{year}.png"
            heat_data = get_base64_img(heat_path)
            if heat_data:
                folium.raster_layers.ImageOverlay(heat_data, bounds=bounds, opacity=opacity).add_to(m)

        if GEOJSON_PATH.exists():
            with open(GEOJSON_PATH, "r") as f: gj = json.load(f)
            folium.GeoJson(gj, style_function=lambda x: {'fillColor': 'none', 'color': '#333', 'weight': 2}).add_to(m)
        
        folium_static(m, width=850, height=600)

    with col_stats:
        diff = year - 2026
        st.subheader(f"Stanje: {year}.")
        st.metric("Nove urbane zone", f"+{diff * 5.2:.1f} ha")
        st.metric("Gubitak biomase", f"-{diff * 1400:,} stabala")
        st.metric("Toplinski otok", f"+{(diff/24)*2.5:.1f} °C")
        # Zamijeni st.warning u col_stats ovim kodom:
        if year < 2035:
            st.success("✅ Faza: Rana urbanizacija - fokus na rubnim zonama.")
        elif 2035 <= year < 2045:
            st.warning("⚠️ Faza: Intenzivna izgradnja - pritisak na gradske četvrti.")
        else:
            st.error("🚨 Faza: Kritična degradacija - značajan gubitak zelenih površina.")
        