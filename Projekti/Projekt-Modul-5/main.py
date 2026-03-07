# -*- coding: utf-8 -*-
"""
Jednostavan parking demo (annotator + YOLO occupancy)
- Annotator: drag-rectangle na 1. frameu (S=save, U=undo, C=clear, ENTER=start, ESC=exit)
- YOLO: predict per frame (stabilno uz pauzu), bez bbox crteža
- Occupancy: OVERLAP metoda (umjesto center-in-polygon) + blaga dilatacija maski
- HUD: FREE/OCC u gornjoj crnoj traci, kontrole u donjoj crnoj traci
- Pauza: SPACE (ESC=exit)
"""

import os
import json
import numpy as np
import cv2
import cvzone
from ultralytics import YOLO
from pathlib import Path

# ---------------------------
# CONFIG
# ---------------------------

ROOT = Path(__file__).resolve().parent
VIDEO     = str(ROOT / "videos" / "vid.mp4")
WEIGHTS   = str(ROOT / "runs" / "detect" / "runs_yolo" / "v2_yolov8s" / "weights" / "best.pt")
POLY_JSON = str(ROOT / "polygons" / "polygons.json")

DISPLAY_W, DISPLAY_H = 1020, 500   # prikazna rezolucija (UI)
IMG_SIZE  = 1536                   # višekratnik 32 (npr. 1024/1536/1600/1920)
CONF_THR  = 0.18                   # po potrebi 0.18 za još veći recall

# Overlap metodologija (umjesto centra): 
# Auto koji stoji “na liniji” → centar upadne van → slot označi kao FREE iako je zauzet
OVERLAP_THR = 0.12                 # 0.10–0.15 tipično dobro za top-down
DILATE_PX   = 3                    # rubna tolerancija maski u DISPLAY pikselima (2–4 OK)

# HUD trake:
HEADER_H = 42                      # gornja traka (FREE/OCC)
FOOTER_H = 34                      # donja traka (kontrole)

# ---------------------------
# UČITAJ VIDEO I MODEL
# ---------------------------
cap0 = cv2.VideoCapture(VIDEO)
ok, frame0 = cap0.read()
cap0.release()
if not ok:
    raise RuntimeError("Ne mogu pročitati video!")

orig_h, orig_w = frame0.shape[:2]
sx = DISPLAY_W / float(orig_w)
sy = DISPLAY_H / float(orig_h)
inv_sx = orig_w / float(DISPLAY_W)
inv_sy = orig_h / float(DISPLAY_H)

model = YOLO(WEIGHTS)

# ---------------------------
# POMOĆNE FUNKCIJE
# ---------------------------
def to_display(pts):
    """Pretvori točke iz ORIGINAL u DISPLAY koordinatni sustav."""
    return [[int(x * sx), int(y * sy)] for x, y in pts]

def to_original(pt):
    x, y = pt
    return int(x * inv_sx), int(y * inv_sy)

def order_rect(x1, y1, x2, y2):
    L, R = sorted([x1, x2])
    T, B = sorted([y1, y2])
    return [[L, T], [R, T], [R, B], [L, B]]

def load_polys(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_polys(path, polys):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(polys, f, ensure_ascii=False, indent=2)

def build_slot_masks(polygons_disp, H, W, dilate_px=0):
    """0/255 maske za svaki slot u DISPLAY rezoluciji; opcijski rubno proširenje."""
    masks = []
    for poly in polygons_disp:
        m = np.zeros((H, W), dtype=np.uint8)
        cnt = np.array(poly, np.int32).reshape((-1, 1, 2))
        cv2.fillPoly(m, [cnt], 255)
        if dilate_px > 0:
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * dilate_px + 1, 2 * dilate_px + 1))
            m = cv2.dilate(m, k, iterations=1)
        masks.append(m)
    return masks

def overlap_ratio(mask, x1, y1, x2, y2):
    """Postotak bbox-a unutar maske (0..1). Koordinate moraju biti u DISPLAY prostoru."""
    H, W = mask.shape[:2]
    x1 = max(0, min(W - 1, int(x1))); x2 = max(0, min(W - 1, int(x2)))
    y1 = max(0, min(H - 1, int(y1))); y2 = max(0, min(H - 1, int(y2)))
    if x2 <= x1 or y2 <= y1:
        return 0.0
    sub = mask[y1:y2, x1:x2]
    inside = int((sub == 255).sum())
    area   = (x2 - x1) * (y2 - y1)
    return inside / max(1, area)

def draw_header_hud(img, free, occ):
    """FREE/OCC u gornjoj crnoj traci."""
    H, W = img.shape[:2]
    cv2.rectangle(img, (0, 0), (W, HEADER_H), (0, 0, 0), thickness=-1)
    # FREE (lijevo)
    cvzone.putTextRect(
        img, f"FREE: {free}", (16, 10 + 22), 1, 2, colorT=(255, 255, 255),
        colorR=(180, 0, 255), colorB=(0, 0, 0), border=0
    )
    # OCC (desno)
    txt = f"OCC: {occ}"
    (tw, _), _ = cv2.getTextSize(txt, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
    cvzone.putTextRect(
        img, txt, (W - 16 - tw - 12, 10 + 22), 1, 2, colorT=(255, 255, 255),
        colorR=(255, 0, 128), colorB=(0, 0, 0), border=0
    )

def draw_footer_hud(img, text_left="SPACE=pauza/play", text_right="ESC=exit"):
    """Kontrole u donjoj crnoj traci."""
    H, W = img.shape[:2]
    y1 = H - FOOTER_H
    cv2.rectangle(img, (0, y1), (W, H), (0, 0, 0), thickness=-1)
    # lijevi tekst
    cv2.putText(img, text_left, (10, H - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    # desni tekst
    (tw, _), _ = cv2.getTextSize(text_right, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    cv2.putText(img, text_right, (W - 10 - tw, H - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

# ---------------------------
# ANOTACIJA (drag rectangle na 1. frameu)
# ---------------------------
polygons = load_polys(POLY_JSON)   # poligoni u ORIGINALNOJ rezoluciji
dragging, p0, p1 = False, None, None

win = "Annotator (drag rectangle)  S=save, U=undo, C=clear, ENTER=start YOLO"
cv2.namedWindow(win, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win, DISPLAY_W, DISPLAY_H)

def on_mouse(event, x, y, flags, param):
    global dragging, p0, p1, polygons
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True; p0 = (x, y); p1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        p1 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP and dragging:
        dragging = False
        if p0 and p1:
            x1o, y1o = to_original(p0)
            x2o, y2o = to_original(p1)
            if abs(x2o - x1o) > 5 and abs(y2o - y1o) > 5:
                polygons.append(order_rect(x1o, y1o, x2o, y2o))
        p0 = p1 = None

cv2.setMouseCallback(win, on_mouse)

# Annotator petlja
while True:
    disp = cv2.resize(frame0, (DISPLAY_W, DISPLAY_H))

    # postojeći poligoni (zelena)
    for poly in polygons:
        pts_disp = np.array(to_display(poly), np.int32).reshape((-1, 1, 2))
        cv2.polylines(disp, [pts_disp], True, (0, 255, 0), 2)

    # preview pravokutnika
    if dragging and p0 and p1:
        cv2.rectangle(disp, p0, p1, (0, 165, 255), 2)

    cv2.putText(disp, "S=save  U=undo  C=clear  ENTER=start detection",
                (10, HEADER_H + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow(win, disp)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        raise SystemExit(0)
    elif k in (ord('s'), ord('S')):
        save_polys(POLY_JSON, polygons)
        print(f"[INFO] Spremljeno: {POLY_JSON} (slots={len(polygons)})")
    elif k in (ord('u'), ord('U')):
        if polygons:
            polygons.pop()
    elif k in (ord('c'), ord('C')):
        polygons = []
    elif k == 13:   # ENTER
        break

# ---------------------------
# YOLO + OVERLAP OCCUPANCY (pauza na SPACE)
# ---------------------------
print("Pokrećem YOLO...")

# Pretvori poligone u DISPLAY koordinate i pripremi maske (s dilatacijom ruba)
polygons_disp = [to_display(p) for p in polygons]
slot_masks    = build_slot_masks(polygons_disp, DISPLAY_H, DISPLAY_W, dilate_px=DILATE_PX)

cap = cv2.VideoCapture(VIDEO)
paused = False
last_disp = None

while True:
    if not paused:
        ok, frame = cap.read()
        if not ok:
            break
        disp = cv2.resize(frame, (DISPLAY_W, DISPLAY_H))
        last_disp = disp.copy()
    else:
        if last_disp is None:
            ok, frame = cap.read()
            if not ok:
                break
            last_disp = cv2.resize(frame, (DISPLAY_W, DISPLAY_H))
        disp = last_disp.copy()

    # YOLO detekcija (bez trackinga; stabilno dok je pauza)
    # IOU = Ako se dva bounding boxa preklapaju ≥ 50%, smatraj ih duplikatima i zadrži samo onaj s većim confidenceom
    res = model.predict(disp, imgsz=IMG_SIZE, conf=CONF_THR, iou=0.50, verbose=False)
    r = res[0]

    # Poligone prvo iscrtaj zeleno
    for pts in polygons_disp:
        cnt = np.array(pts, np.int32).reshape((-1, 1, 2))
        cv2.polylines(disp, [cnt], True, (0, 255, 0), 2)

    # Dohvati BBOX-ove
    boxes = None
    if r.boxes is not None and r.boxes.xyxy is not None and len(r.boxes) > 0:
        boxes = r.boxes.xyxy.cpu().numpy().astype(int)

    # Izračun zauzeća preko OVERLAP-a
    occ_flags = [False] * len(polygons_disp)
    if boxes is not None:
        for (x1, y1, x2, y2) in boxes:
            for si, mask in enumerate(slot_masks):
                if not occ_flags[si] and overlap_ratio(mask, x1, y1, x2, y2) >= OVERLAP_THR:
                    occ_flags[si] = True

    # Oboji crveno zauzete
    for si, pts in enumerate(polygons_disp):
        if occ_flags[si]:
            cnt = np.array(pts, np.int32).reshape((-1, 1, 2))
            cv2.polylines(disp, [cnt], True, (0, 0, 255), 2)

    occupied = sum(1 for v in occ_flags if v)
    free     = len(polygons_disp) - occupied

    # HUD: gore FREE/OCC, dolje kontrole
    draw_header_hud(disp, free, occupied)
    draw_footer_hud(disp, "SPACE=pauza/play", "ESC=exit")

    cv2.imshow(win, disp)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord(' '):
        paused = not paused

cap.release()
cv2.destroyAllWindows()