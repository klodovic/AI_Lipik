# ============================================================
# Sentinel‑2 L2A (STAC + OData S3Path → S3 download of JP2 bands)
# Layout: flat | by-year | by-year-tile  (default: by-year-tile)
#  - STAC inventory (paging, cloud filter, optional AOI)
#  - OData catalog → S3Path (Name eq ... → fallback startswith(...))
#  - S3 (eodata.dataspace.copernicus.eu) download of B04/B08/SCL
#  - Resume per file (.part), tqdm progress, logging, counters
#  - .env: CDSE_S3_KEY, CDSE_S3_SECRET
# ============================================================

import os
import re
import json
import argparse
import logging
from pathlib import Path
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional, Iterator, Dict, List, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
import fsspec

# --------------------------- Logging ---------------------------
log = logging.getLogger("s2s3")

def setup_logging(log_path: Optional[str]):
    log.setLevel(logging.INFO)
    log.handlers[:] = []
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s",
                            "%Y-%m-%d %H:%M:%S")

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    ch.setLevel(logging.INFO)
    log.addHandler(ch)

    if log_path:
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setFormatter(fmt)
        fh.setLevel(logging.INFO)
        log.addHandler(fh)

# --------------------------- HTTP session ----------------------
def make_session() -> requests.Session:
    s = requests.Session()
    retries = Retry(
        total=6,
        backoff_factor=1.2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    ad = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=20)
    s.mount("https://", ad)
    s.mount("http://", ad)
    return s

# --------------------------- AOI loader ------------------------
def load_aoi_geojson(path: Optional[str]) -> Optional[dict]:
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    try:
        gj = json.load(open(p, "r", encoding="utf-8"))
        if gj.get("type") == "FeatureCollection":
            feats = gj.get("features") or []
            return feats[0].get("geometry") if feats else None
        if gj.get("type") == "Feature":
            return gj.get("geometry")
        return gj
    except Exception:
        return None

# --------------------------- STAC search -----------------------
STAC_URL = "https://stac.dataspace.copernicus.eu/v1/search"
COLLECTION = "sentinel-2-l2a"

def stac_search(session: requests.Session,
                start: str, end: str, max_cloud: float,
                aoi_geojson: Optional[dict],
                page_limit: int) -> Iterator[dict]:
    body = {
        "collections": [COLLECTION],
        "datetime": f"{start}T00:00:00Z/{end}T23:59:59Z",
        "limit": page_limit,
        "query": {"eo:cloud_cover": {"lte": max_cloud}},
        "sortby": [{"field": "properties.datetime", "direction": "asc"}],
        "fields": {
            "include": [
                "id", "assets", "links",
                "properties.datetime",
                "properties.s2:mgrs_tile",
                "properties.eo:cloud_cover"
            ]
        }
    }
    if aoi_geojson:
        body["intersects"] = aoi_geojson

    log.info(f"[STAC] POST search {start}→{end}, cloud<={max_cloud}%")
    r = session.post(STAC_URL, json=body, timeout=90)
    r.raise_for_status()
    js = r.json()

    feats = js.get("features") or []
    log.info(f"[STAC] page 1: {len(feats)} item(s)")
    for f in feats:
        yield f

    while True:
        next_link = None
        for ln in js.get("links") or []:
            if ln.get("rel") == "next":
                next_link = ln.get("href")
                break
        if not next_link:
            return
        r = session.get(next_link, timeout=60)
        r.raise_for_status()
        js = r.json()
        feats = js.get("features") or []
        log.info(f"[STAC] next page: {len(feats)} item(s)")
        for f in feats:
            yield f

# ----------------------- OData: resolve S3Path -----------------
CATALOG_ODATA = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"

def odata_get_s3path_by_name(session: requests.Session, pid: str) -> Optional[str]:
    """
    Try exact Name (pid, pid+'.SAFE'), then fallback startswith(Name,pid).
    Returns S3Path (string like 'eodata/.../SAFE') or None.
    """
    # 1) Exact match
    for nm in (pid, f"{pid}.SAFE"):
        url = (f"{CATALOG_ODATA}"
               f"?$filter=Name eq '{nm}'"
               f"&$select=Id,Name,S3Path&$top=1")
        r = session.get(url, timeout=60)
        if r.ok:
            js = r.json()
            vals = js.get("value") or []
            if vals:
                sp = vals[0].get("S3Path")
                if sp:
                    return sp

    # 2) startswith(Name, pid)
    url = (f"{CATALOG_ODATA}"
           f"?$filter=startswith(Name,'{pid}')"
           f"&$select=Id,Name,S3Path&$top=1")
    r = session.get(url, timeout=60)
    if r.ok:
        js = r.json()
        vals = js.get("value") or []
        if vals:
            return vals[0].get("S3Path")
    return None

# ----------------------- S3 filesystem -------------------------
def make_s3fs():
    key = os.getenv("CDSE_S3_KEY") or os.getenv("AWS_ACCESS_KEY_ID")
    secret = os.getenv("CDSE_S3_SECRET") or os.getenv("AWS_SECRET_ACCESS_KEY")
    if not key or not secret:
        raise RuntimeError("S3 kredencijali nisu postavljeni (.env: CDSE_S3_KEY / CDSE_S3_SECRET).")
    fs = fsspec.filesystem(
        "s3",
        key=key,
        secret=secret,
        client_kwargs={
            "endpoint_url": "https://eodata.dataspace.copernicus.eu",
            "region_name": "default"
        },
    )
    return fs

# ----------------------- Helpers: list / download --------------
def list_all_keys(fs, prefix: str) -> List[str]:
    """
    List recursively all objects under prefix.
    Accepts prefixes starting with '/', 'eodata/', or bare.
    """
    sp = prefix.strip().lstrip("/")
    if not sp.lower().startswith("eodata/"):
        sp = f"eodata/{sp}"
    try:
        return fs.find(sp)
    except Exception:
        out = []
        for p, _, files in fs.walk(sp):
            out.extend([f"{p.rstrip('/')}/{f}" for f in files])
        return out

def download_one(fs, s3key: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(out_path.suffix + ".part")
    start = tmp.stat().st_size if tmp.exists() else 0

    size = None
    try:
        info = fs.info(s3key)
        size = info.get("Size") or info.get("size")
    except Exception:
        size = None

    mode = "ab" if start > 0 else "wb"
    with fs.open(s3key, "rb") as src, open(tmp, mode) as dst:
        with tqdm(total=size, initial=start if size else 0,
                  unit="B", unit_scale=True,
                  desc=out_path.name[:28], leave=True) as pbar:
            if start > 0:
                src.seek(start)
            while True:
                chunk = src.read(16 * 1024 * 1024)
                if not chunk:
                    break
                dst.write(chunk)
                pbar.update(len(chunk))
    os.replace(tmp, out_path)

# ----------------------- Layout helpers ------------------------
_TILE_FROM_ID = re.compile(r"_T(\d{2}[A-Z]{3})_")

def infer_tile(pid: str) -> str:
    m = _TILE_FROM_ID.search(pid or "")
    return f"T{m.group(1)}" if m else "TXXXX"

def target_output_dir(base: Path, layout: str, pid: str, props: dict) -> Path:
    """
    layout: 'flat' | 'by-year' | 'by-year-tile'
    """
    dt_iso = (props or {}).get("datetime") or ""
    year = (dt_iso[:4] if len(dt_iso) >= 4 else "YYYY")
    tile = (props or {}).get("s2:mgrs_tile") or infer_tile(pid)

    if layout == "flat":
        return base
    if layout == "by-year":
        return base / year
    if layout == "by-year-tile":
        return base / year / tile
    return base  # fallback

# ----------------------- Counters ------------------------------
#WANTED = ("_B04_10m.jp2", "_B08_10m.jp2", "_SCL_20m.jp2")
#WANTED = ("_B04_10m.jp2", "_B08_10m.jp2", "_B11_20m.jp2", "_SCL_20m.jp2")
WANTED = ("_B02_10m.jp2", "_B03_10m.jp2")

class Cnt:
    def __init__(self):
        self.scanned = 0
        self.ok = 0
        self.err = 0
        self.cloud_sum = 0.0
        self.cloud_n = 0

# ----------------------- Process item --------------------------
def process_item(session: requests.Session, fs, item: dict, out_dir: Path,
                 lock: Lock, cnt: Cnt, layout: str):
    pid = item.get("id")
    props = item.get("properties") or {}
    dt = props.get("datetime")
    cloud = props.get("eo:cloud_cover")
    tile = props.get("s2:mgrs_tile") or infer_tile(pid or "")

    with lock:
        cloud_txt = f"{cloud:.2f}%" if isinstance(cloud, (int, float)) else "n/a"
        log.info(f"▶ {pid} | {dt} | tile={tile} | cloud={cloud_txt}")

    # 1) OData → S3Path
    s3path = odata_get_s3path_by_name(session, pid)
    if not s3path:
        with lock:
            log.error(f"{pid}: OData S3Path NOT FOUND")
            cnt.err += 1
        return

    # normalize prefix
    sp = s3path.strip().lstrip("/")
    if not sp.lower().startswith("eodata/"):
        sp = f"eodata/{sp}"

    # 2) find band objects
    keys = list_all_keys(fs, sp)
    targets: List[Tuple[str, Path]] = []
    for suf in WANTED:
        cand = [k for k in keys if k.endswith(suf)]
        if not cand:
            # for SCL search more loosely
            if suf == "_SCL_20m.jp2":
                cand = [k for k in keys if k.endswith("SCL_20m.jp2")]
        if not cand:
            with lock:
                log.error(f"{pid}: missing {suf}")
                cnt.err += 1
            return
        k = cand[0]

        # 3) compute output dir by layout
        out_dir_final = target_output_dir(out_dir, layout, pid, props)
        out_dir_final.mkdir(parents=True, exist_ok=True)

        outp = out_dir_final / Path(k).name
        targets.append((k, outp))

    # 4) download
    for k, outp in targets:
        if not outp.exists():
            download_one(fs, k, outp)

    with lock:
        cnt.ok += 1
        if isinstance(cloud, (int, float)):
            cnt.cloud_sum += float(cloud)
            cnt.cloud_n += 1

# ----------------------- RUN -----------------------------------
def run(start: str, end: str, max_cloud: float, aoi_geojson: Optional[str],
        out_dir: str, workers: int, page_limit: int, log_file: Optional[str],
        layout: str):

    setup_logging(log_file)
    log.info("=== S2 S3 downloader (STAC + OData S3Path → S3) ===")
    log.info(f"layout={layout}")

    session = make_session()
    fs = make_s3fs()

    out_p = Path(out_dir)
    out_p.mkdir(parents=True, exist_ok=True)

    aoi = load_aoi_geojson(aoi_geojson)
    items = stac_search(session, start, end, max_cloud, aoi, page_limit)

    lock = Lock()
    cnt = Cnt()

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = []
        for it in items:
            with lock:
                cnt.scanned += 1
            futs.append(pool.submit(process_item, session, fs, it, out_p, lock, cnt, layout))
        for f in as_completed(futs):
            try:
                _ = f.result()
            except Exception as e:
                with lock:
                    cnt.err += 1
                    log.error(f"worker error: {e}")

    log.info("--------------- SUMMARY ---------------")
    log.info(f"scanned : {cnt.scanned}")
    log.info(f"ok      : {cnt.ok}")
    log.info(f"errors  : {cnt.err}")
    if cnt.cloud_n > 0:
        log.info(f"avg cloud: {cnt.cloud_sum/cnt.cloud_n:.2f}%")

# ----------------------- CLI -----------------------------------
def main():
    ap = argparse.ArgumentParser(description="S2 L2A JP2 downloader via STAC + OData(S3Path) + S3")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--max-cloud", type=float, default=20)
    ap.add_argument("--aoi", default=None, help="AOI GeoJSON (optional)")
    ap.add_argument("--out", required=True, help="Output folder (root)")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--page-limit", type=int, default=200)
    ap.add_argument("--log", default=None)
    ap.add_argument("--layout", choices=["flat", "by-year", "by-year-tile"],
                    default="by-year-tile",
                    help="Organizacija izlaza (default: by-year-tile)")
    args = ap.parse_args()

    run(
        start=args.start,
        end=args.end,
        max_cloud=args.max_cloud,
        aoi_geojson=args.aoi,
        out_dir=args.out,
        workers=args.workers,
        page_limit=args.page_limit,
        log_file=args.log,
        layout=args.layout,
    )

if __name__ == "__main__":
    main()

"""

# 2016

python -m data.s_jp2_downloader `
  --start 2016-01-01 `
  --end 2016-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2016.log"


# 2017
python -m data.s_jp2_downloader `
  --start 2017-01-01 `
  --end 2017-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2017.log"

# 2018

python -m data.s_jp2_downloader `
  --start 2018-01-01 `
  --end 2018-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2018.log"

  
# 2019

python -m data.s_jp2_downloader `
  --start 2019-01-01 `
  --end 2019-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2019.log"

  
# 2020
python -m data.s_jp2_downloader `
  --start 2020-01-01 `
  --end 2020-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2020.log"

# 2021
python -m data.s_jp2_downloader `
  --start 2021-01-01 `
  --end 2021-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2021.log"


# 2022
python -m data.s_jp2_downloader `
  --start 2022-01-01 `
  --end 2022-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2022.log"

# 2023
python -m data.s_jp2_downloader `
  --start 2023-01-01 `
  --end 2023-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2023.log"

# 2024
python -m data.s_jp2_downloader `
  --start 2024-01-01 `
  --end 2024-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2024.log"


# 2025
python -m data.s_jp2_downloader `
  --start 2025-01-01 `
  --end 2025-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2025.log"

# 2026
python -m data.s_jp2_downloader `
  --start 2026-01-01 `
  --end 2026-12-31 `
  --max-cloud 20 `
  --aoi "D:\copernicus-zagreb\data\reference\aoi_zagreb.geojson" `
  --out "D:\copernicus-zagreb\data\raw\sentinel2" `
  --workers 4 `
  --page-limit 200 `
  --layout by-year-tile `
  --log "D:\copernicus-zagreb\logs\s2_s3_2026.log"


"""