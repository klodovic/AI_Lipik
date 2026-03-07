
# Parking Occupancy Detection (YOLOv8 + Polygon Overlap)

Jednostavan i robustan sustav za **detekciju zauzetosti parkirnih mjesta** iz **top‑down videa**.
Projekt koristi **YOLOv8** (Ultralytics) za detekciju vozila i **overlap metodologiju** nad ručno definiranim pravokutnim poligonima.

## ✨ Značajke
- Annotator (2‑click rectangle)
- YOLO predict po frameu
- Occupancy metodologija: OVERLAP + dilatacija maski
- HUD: FREE/OCC (gore) + kontrole (dolje)
- SPACE pauza/play, ESC izlaz

## 📦 Struktura projekta
```
Projekt-Modul-5/
├─ main.py
├─ models/best.pt
├─ videos/vid1.mp4
├─ polygons/polygons.json
├─ output/
└─ README.md
```

## 🚀 Pokretanje
```bash
python main.py
```
- Annotator: S=save, U=undo, C=clear, ENTER=start, ESC=exit
- YOLO: SPACE pauza/play, ESC izlaz

## ⚙️ Ključne postavke
```python
IMG_SIZE    = 1920
CONF_THR    = 0.20
OVERLAP_THR = 0.12
DILATE_PX   = 3
```

## 🧠 Metodologija: Overlap
1. Slot → binarna maska
2. Dilatacija rubova: 3 px
3. overlap = (BBOX ∩ maska) / (površina BBOX‑a)
4. Ako ≥ OVERLAP_THR → zauzeto

## 📈 Rezultati modela
- Precision ≈ 0.95–1.00
- Recall ≈ 0.95–1.00
- mAP@50 ≈ 0.98–0.99
- mAP@50–95 ≈ 0.90

## 👤 Autor
Josip Smoljić — 2026.
