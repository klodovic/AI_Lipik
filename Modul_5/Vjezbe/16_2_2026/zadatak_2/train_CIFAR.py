import time
from dataclasses import dataclass
from typing import Tuple

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms

from model_cifar import CifarCNN


@dataclass
class Config:
    batch_size: int = 128
    epochs: int = 15
    lr: float = 1e-3
    val_fraction: float = 0.10
    seed: int = 42
    image_size: Tuple[int, int] = (32, 32)
    num_workers: int = 4
    log_dir: str = "./runs/cifar10_cnn"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


def set_seed(seed: int) -> None:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_cifar10(image_size: Tuple[int, int]):
    # Standardna CIFAR-10 normalizacija
    mean = (0.4914, 0.4822, 0.4465)
    std = (0.2023, 0.1994, 0.2010)

    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])

    dataset = datasets.CIFAR10(
        root="./data",
        train=True,
        download=True,
        transform=transform,
    )
    return dataset


def split_dataset(dataset, val_fraction: float, seed: int):
    total_size = len(dataset)
    val_size = int(total_size * val_fraction)
    train_size = total_size - val_size

    g = torch.Generator().manual_seed(seed)
    train_ds, val_ds = random_split(dataset, [train_size, val_size], generator=g)
    return train_ds, val_ds


def train_one_epoch(model, loader, criterion, optimizer, device) -> float:
    model.train()
    running_loss = 0.0

    for images, targets in loader:
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)
        logits = model(images)
        loss = criterion(logits, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    return running_loss / len(loader.dataset)


@torch.no_grad()
def validate(model, loader, device) -> float:
    model.eval()
    correct = 0
    total = 0

    for images, targets in loader:
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        logits = model(images)
        preds = torch.argmax(logits, dim=1)

        correct += (preds == targets).sum().item()
        total += targets.size(0)

    return correct / max(1, total)


def main():
    cfg = Config()
    set_seed(cfg.seed)

    device = torch.device(cfg.device)
    print(f"Device: {device}")

    # 1) Load CIFAR-10
    dataset = load_cifar10(cfg.image_size)

    # 2) Train/Val split
    train_ds, val_ds = split_dataset(dataset, cfg.val_fraction, cfg.seed)

    train_loader = DataLoader(
        train_ds,
        batch_size=cfg.batch_size,
        shuffle=True,
        num_workers=cfg.num_workers,
        pin_memory=True,
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=cfg.batch_size,
        shuffle=False,
        num_workers=cfg.num_workers,
        pin_memory=True,
    )

    num_classes = 10
    print(f"Train size: {len(train_ds)} | Val size: {len(val_ds)}")

    # -------------------------------------------------
    # 3) TODO: konstrukcija modela
    # -------------------------------------------------
    #
    # -------------------------------------------------

    model = CifarCNN(num_classes=num_classes, in_channels=3).to(device)

    # 4) Ispis slojeva
    print("\nArhitektura modela:")
    print(model)

    # Sanity check: provjera izlaznog oblika
    sample_x, _ = next(iter(train_loader))
    sample_x = sample_x.to(device)
    with torch.no_grad():
        out = model(sample_x)
    if out.ndim != 2 or out.shape[1] != num_classes:
        raise RuntimeError(f"Output mora biti [B, {num_classes}], dobiveno: {tuple(out.shape)}")

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.lr)

    writer = SummaryWriter(cfg.log_dir)

    # 5) Trening + validacija
    for epoch in range(1, cfg.epochs + 1):
        t0 = time.time()

        train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        val_acc = validate(model, val_loader, device)

        # 6) Loganje (minimalno)
        writer.add_scalar("train/loss", train_loss, epoch)
        writer.add_scalar("val/accuracy", val_acc, epoch)

        print(
            f"Epoch {epoch:02d}/{cfg.epochs} | "
            f"Train Loss: {train_loss:.4f} | "
            f"Val Acc: {val_acc*100:.2f}% | "
            f"Time: {time.time() - t0:.1f}s"
        )

    writer.close()
    print("Trening završen.")


if __name__ == "__main__":
    main()
