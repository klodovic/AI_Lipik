import time
from dataclasses import dataclass
from typing import Tuple

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms    

import model_student as model


# -------------------------------------------------
# Konfiguracija
# -------------------------------------------------
@dataclass
class Config:
    batch_size: int = 64
    epochs: int = 5
    lr: float = 1e-3
    val_fraction: float = 0.10
    seed: int = 42
    image_size: Tuple[int, int] = (28, 28)
    log_dir: str = "./runs/mnist_cnn"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


def set_seed(seed: int):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


# -------------------------------------------------
# Dataset
# -------------------------------------------------
def load_mnist(image_size):
    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
    ])

    dataset = datasets.MNIST(
        root="./data",
        train=True,
        download=True,
        transform=transform,
    )

    return dataset


def split_dataset(dataset, val_fraction, seed):
    total_size = len(dataset)
    val_size = int(total_size * val_fraction)
    train_size = total_size - val_size

    generator = torch.Generator().manual_seed(seed)
    train_ds, val_ds = random_split(dataset, [train_size, val_size], generator=generator)

    return train_ds, val_ds


# -------------------------------------------------
# Trening / validacija
# -------------------------------------------------
def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0

    for images, targets in loader:
        images = images.to(device)
        targets = targets.to(device)

        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    return running_loss / len(loader.dataset)


@torch.no_grad()
def validate(model, loader, device):
    model.eval()
    correct = 0
    total = 0

    for images, targets in loader:
        images = images.to(device)
        targets = targets.to(device)

        logits = model(images)
        preds = torch.argmax(logits, dim=1)

        correct += (preds == targets).sum().item()
        total += targets.size(0)

    return correct / total


# -------------------------------------------------
# Main
# -------------------------------------------------
def main():
    cfg = Config()
    set_seed(cfg.seed)

    device = torch.device(cfg.device)
    print(f"Device: {device}")

    # 1) Load MNIST
    dataset = load_mnist(cfg.image_size)

    # 2) Train/Val split
    train_ds, val_ds = split_dataset(dataset, cfg.val_fraction, cfg.seed)

    train_loader = DataLoader(train_ds, batch_size=cfg.batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=cfg.batch_size, shuffle=False)

    num_classes = 10  # MNIST ima 10 klasa (0-9)

    # -------------------------------------------------
    # 3) TODO: pozvati konstruktor modela
    #
    # -------------------------------------------------

    # 4) Ispis slojeva mreže
    print("\nArhitektura modela:")
    print(model)

    # Sanity check
    sample_x, _ = next(iter(train_loader))
    sample_x = sample_x.to(device)
    with torch.no_grad():
        out = model(sample_x)
    if out.shape[1] != num_classes:
        raise RuntimeError(f"Output mora biti [B, {num_classes}]")

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.lr)

    writer = SummaryWriter(cfg.log_dir)

    # -------------------------------------------------
    # 5) Trening i validacija
    # -------------------------------------------------
    for epoch in range(1, cfg.epochs + 1):
        start = time.time()

        train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        val_acc = validate(model, val_loader, device)

        # 6) Loganje
        writer.add_scalar("train/loss", train_loss, epoch)
        writer.add_scalar("val/accuracy", val_acc, epoch)

        print(
            f"Epoch {epoch}/{cfg.epochs} | "
            f"Train Loss: {train_loss:.4f} | "
            f"Val Acc: {val_acc*100:.2f}% | "
            f"Time: {time.time() - start:.1f}s"
        )

    writer.close()
    print("Trening završen.")


if __name__ == "__main__":
    main()
