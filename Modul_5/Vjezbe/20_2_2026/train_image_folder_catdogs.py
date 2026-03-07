from pathlib import Path
from typing import Tuple

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torchvision.models import resnet18, ResNet18_Weights


# =========================
# GLOBALNE POSTAVKE
# =========================
DATA_ROOT = Path("PetImages")
RUN_DIR = Path("runs/catsdogs_imagefolder")

EPOCHS = 5
BATCH_SIZE = 32
LEARNING_RATE = 1e-3
NUM_WORKERS = 4

VAL_RATIO = 0.10
SEED = 42

LOG_EVERY = 10


def make_dataloaders_with_imagefolder() -> Tuple[DataLoader, DataLoader, int]:
    if not DATA_ROOT.exists():
        raise FileNotFoundError(f"Ne nalazim: {DATA_ROOT}")

    weights = ResNet18_Weights.DEFAULT

    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.ToTensor(),
        transforms.Normalize(mean=weights.transforms().mean, std=weights.transforms().std),
    ])

    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=weights.transforms().mean, std=weights.transforms().std),
    ])

    # TODO: Učitati dataset koristeći ImageFolder, podijeliti na train/val i kreirati DataLoadere,


    dataset = ImageFolder(root=DATA_ROOT, transform=train_transform)
    num_classes = len(dataset.classes)
    n_val = int(len(dataset) * VAL_RATIO)
    n_train = len(dataset) - n_val
    train_ds, val_ds = random_split(dataset, [n_train, n_val], generator=torch.Generator().manual_seed(SEED))
    val_ds.dataset.transform = val_transform

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS)

    

    print(f"Split: train={n_train}, val={n_val}")
    return train_loader, val_loader, num_classes


def build_model(num_classes: int) -> nn.Module:
    weights = ResNet18_Weights.DEFAULT
    model = resnet18(weights=weights)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


@torch.no_grad()
def evaluate_accuracy(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    total = 0

    for x, y in loader:
        x = x.to(device, non_blocking=True)
        y = y.to(device, non_blocking=True)

        logits = model(x)
        preds = torch.argmax(logits, dim=1)

        correct += (preds == y).sum().item()
        total += y.numel()

    return (correct / total) if total > 0 else 0.0


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    writer = SummaryWriter(log_dir=str(RUN_DIR / "tb"))

    # ============================================================
    # TODO (za sljedeći zadatak):
    # OBRIŠITE ovaj ImageFolder blok i zamijenite custom datasetom
    # ============================================================
    train_loader, val_loader, num_classes = make_dataloaders_with_imagefolder()
    # ============================================================

    model = build_model(num_classes=num_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    global_step = 0
    best_val_acc = -1.0

    for epoch in range(1, EPOCHS + 1):
        model.train()
        running_loss = 0.0

        for batch_idx, (x, y) in enumerate(train_loader, start=1):
            x = x.to(device, non_blocking=True)
            y = y.to(device, non_blocking=True)

            optimizer.zero_grad(set_to_none=True)
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            global_step += 1

            if batch_idx % LOG_EVERY == 0:
                avg_loss = running_loss / LOG_EVERY
                writer.add_scalar("train/loss", avg_loss, global_step)
                running_loss = 0.0

        val_acc = evaluate_accuracy(model, val_loader, device)
        writer.add_scalar("val/accuracy", val_acc, epoch)

        print(f"Epoch {epoch:02d}/{EPOCHS} | val_acc={val_acc:.4f}")

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(
                {"model_state_dict": model.state_dict(), "num_classes": num_classes},
                RUN_DIR / "best_model.pt",
            )

    writer.close()
    print(f"✅ Trening gotov. Best val_acc={best_val_acc:.4f}")
    print(f"TensorBoard: tensorboard --logdir {RUN_DIR / 'tb'}")


if __name__ == "__main__":
    main()
