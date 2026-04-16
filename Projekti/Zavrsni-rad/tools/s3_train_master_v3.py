import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
import numpy as np
from pathlib import Path
import logging
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

# --- KONFIGURACIJA V3.1 (RTX 3060 OPTIMIZED) ---
BASE_DIR = Path("D:/copernicus-zagreb")
BATCH_DIR = BASE_DIR / "data/batches_train"
MODELS_DIR = BASE_DIR / "model_v3"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_SAVE_PATH = MODELS_DIR / "master_model_v3_final.pth"
LOG_CSV_PATH = MODELS_DIR / "training_stats_v3.csv"
PLOT_PATH_V3 = MODELS_DIR / "v3_metrics_plot.jpg"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
EPOCHS = 180 
BATCH_SIZE = 32 # Tvoja 3060 će ovo pojesti za doručak
LR = 0.0001
PATIENCE = 8 

# --- METRIKA ---
def calculate_dice_acc(pred, target, threshold=0.5, smooth=1e-6):
    pred = (pred > threshold).float()
    target = (target > threshold).float()
    intersection = (pred * target).sum(dim=(2, 3))
    dice = (2. * intersection + smooth) / (pred.sum(dim=(2, 3)) + target.sum(dim=(2, 3)) + smooth)
    return dice.mean().item()

# --- MODEL (ResNet-UNet) ---
class ResBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.BatchNorm2d(channels), nn.ReLU(),
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.BatchNorm2d(channels)
        )
    def forward(self, x): return torch.relu(x + self.conv(x))

class MasterUNet(nn.Module):
    def __init__(self, in_channels=16, out_channels=1):
        super().__init__()
        self.enc1 = nn.Sequential(nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.pool = nn.MaxPool2d(2)
        self.enc2 = nn.Sequential(nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.bottleneck = nn.Sequential(nn.Conv2d(64, 128, 3, padding=1), nn.ReLU())
        self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.dec2 = nn.Sequential(nn.Conv2d(128 + 64, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.dec1 = nn.Sequential(nn.Conv2d(64 + 32, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.final = nn.Sequential(nn.Conv2d(32, 1, 1), nn.Sigmoid())

    def forward(self, x):
        B, S, C, H, W = x.shape
        x_in = x[:, :4].reshape(B, 4*C, H, W) # Sažimanje vremena u kanale
        e1 = self.enc1(x_in); e2 = self.enc2(self.pool(e1))
        b = self.bottleneck(self.pool(e2))
        d2 = self.dec2(torch.cat([self.up(b), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up(d2), e1], dim=1))
        return self.final(d1)

# --- ISPRAVLJENI DATASET ---
class MasterBatchDataset(Dataset):
    def __init__(self, folder): 
        self.files = list(Path(folder).glob("*.npz"))
    def __len__(self): 
        return len(self.files)
    def __getitem__(self, idx):
        # Učitavamo podatak koji je spremljen kao [1, 5, 4, 64, 64]
        data = np.load(self.files[idx])['data']
        if data.ndim == 5 and data.shape[0] == 1:
            data = data[0] # Skidamo prvu dimenziju da ostane [5, 4, 64, 64]
        return torch.from_numpy(data).float()

# --- VIZUALIZACIJA ---
def save_v3_plots(history_df):
    plt.figure(figsize=(15, 6))
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.subplot(1, 2, 1)
    plt.plot(history_df['epoch'], history_df['train_loss'], label='Train Loss')
    plt.plot(history_df['epoch'], history_df['val_loss'], label='Val Loss', linestyle='--')
    plt.title('Loss (MSE)'); plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(history_df['epoch'], history_df['train_acc'], label='Train Acc')
    plt.plot(history_df['epoch'], history_df['val_acc'], label='Val Acc', linestyle='--')
    plt.title('Accuracy (Dice)'); plt.legend()
    plt.savefig(PLOT_PATH_V3); plt.close()

# --- TRENING ---
def train_v3_final():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    full_dataset = MasterBatchDataset(BATCH_DIR)
    train_size = int(0.8 * len(full_dataset))
    val_size = len(full_dataset) - train_size
    train_ds, val_ds = random_split(full_dataset, [train_size, val_size])

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, num_workers=4, pin_memory=True)

    model = MasterUNet().to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()
    
    history = []
    best_val_loss = float('inf')
    epochs_without_improvement = 0

    for epoch in range(1, EPOCHS + 1):
        model.train()
        t_loss, t_acc = 0, 0
        pbar = tqdm(train_loader, desc=f"Epoha {epoch:03d}")
        
        for batch in pbar:
            batch = batch.to(DEVICE, non_blocking=True)
            # Normalizacija
            batch[:, :, 1:] = batch[:, :, 1:] / 10000.0
            batch = torch.nan_to_num(batch, nan=0.0)
            
            # ISPRAVAK: Target je NDVI (kanal 3) zadnje godine (index 4)
            # batch je [B, 5, 4, 64, 64] -> uzimamo [B, 1, 64, 64]
            target = batch[:, 4, 3:4] 
            
            optimizer.zero_grad()
            output = model(batch)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            acc = calculate_dice_acc(output, target)
            t_loss += loss.item()
            t_acc += acc
            pbar.set_postfix({'loss': f"{loss.item():.5f}", 'dice': f"{acc:.2%}"})
        
        # Validacija
        model.eval()
        v_loss, v_acc = 0, 0
        with torch.no_grad():
            for batch in val_loader:
                batch = batch.to(DEVICE, non_blocking=True)
                batch[:, :, 1:] = batch[:, :, 1:] / 10000.0
                batch = torch.nan_to_num(batch, nan=0.0)
                target = batch[:, 4, 3:4]
                out = model(batch)
                v_loss += criterion(out, target).item()
                v_acc += calculate_dice_acc(out, target)

        train_avg_loss = t_loss / len(train_loader)
        train_avg_acc = t_acc / len(train_loader)
        val_avg_loss = v_loss / len(val_loader)
        val_avg_acc = v_acc / len(val_loader)
        
        history.append({
            'epoch': epoch, 'train_loss': train_avg_loss, 'val_loss': val_avg_loss,
            'train_acc': train_avg_acc, 'val_acc': val_avg_acc
        })

        logging.info(f"E{epoch} | Val Loss: {val_avg_loss:.6f} | Val Acc: {val_avg_acc:.2%}")
        save_v3_plots(pd.DataFrame(history))

        if val_avg_loss < best_val_loss:
            best_val_loss = val_avg_loss
            epochs_without_improvement = 0
            torch.save(model.state_dict(), MODEL_SAVE_PATH)
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= PATIENCE:
                logging.warning(f"Early stopping na epohi {epoch}")
                break
        
        torch.cuda.empty_cache()

if __name__ == "__main__":
    train_v3_final()