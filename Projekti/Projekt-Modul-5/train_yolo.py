from ultralytics import YOLO
from pathlib import Path
import torch

DATA = Path("dataset/parking_v2/data.yaml")
PROJECT = "runs_yolo"
NAME = "v2_yolov8s"
MODEL = "yolov8s.pt"

def main():
    model = YOLO(MODEL)
    device = 0 if torch.cuda.is_available() else "cpu"

    results = model.train(
        data=str(DATA),
        epochs=50,
        imgsz=640,
        batch=8,          # smanji na 4 ako je GPU memorija problem
        patience=15,
        device=device,
        project=PROJECT,
        name=NAME,
        save_period=5,
        verbose=True,
        workers=0,        # KLJUČNO na Windowsu za 1455
    )

    best = Path(PROJECT) / "detect" / NAME / "weights" / "best.pt"
    print(f"\n✅ Trening gotov. Najbolji model: {best}")

if __name__ == "__main__":
    main()