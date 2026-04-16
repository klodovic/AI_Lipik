import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" # Fiks za OpenMP grešku

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

# --- KONFIGURACIJA ---
BASE_DIR = Path("D:/copernicus-zagreb")
BATCH_DIR = BASE_DIR / "data/batches_train"
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_SAVE_PATH = MODELS_DIR / "master_model_v2.pth"
LOG_CSV_PATH = MODELS_DIR / "training_stats.csv"
PLOT_PATH = MODELS_DIR / "loss_plot.png"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
EPOCHS = 50
LR = 0.0001 # Smanjen LR za bolju stabilnost
PATIENCE = 7 # Malo više strpljenja s obzirom na manji LR

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
    def __init__(self, in_channels=16, out_channels=4):
        super().__init__()
        self.enc1 = nn.Sequential(nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.pool = nn.MaxPool2d(2)
        self.enc2 = nn.Sequential(nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.bottleneck = nn.Sequential(nn.Conv2d(64, 128, 3, padding=1), nn.ReLU())
        self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.dec2 = nn.Sequential(nn.Conv2d(128 + 64, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.dec1 = nn.Sequential(nn.Conv2d(64 + 32, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.final = nn.Sequential(nn.Conv2d(32, out_channels, 1), nn.Sigmoid())

    def forward(self, x):
        B, S, C, H, W = x.shape
        x_in = x[:, :4].reshape(B, 4*C, H, W) # 4 godine * 4 kanala
        e1 = self.enc1(x_in); e2 = self.enc2(self.pool(e1))
        b = self.bottleneck(self.pool(e2))
        d2 = self.dec2(torch.cat([self.up(b), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up(d2), e1], dim=1))
        return self.final(d1)

# --- POMOĆNE FUNKCIJE ---
def save_plots(history):
    plt.figure(figsize=(10, 5))
    plt.plot(history['epoch'], history['train_loss'], label='Train Loss')
    plt.plot(history['epoch'], history['val_loss'], label='Val Loss')
    plt.xlabel('Epoch'); plt.ylabel('Loss (MSE)')
    plt.yscale('log') # Logaritamska skala jer loss može jako pasti
    plt.title('Training & Validation Progress')
    plt.legend(); plt.grid(True)
    plt.savefig(PLOT_PATH)
    plt.close()

def visualize_prediction(epoch, model, batch_data):
    model.eval()
    with torch.no_grad():
        # Uzmi prvi primjer i normaliziraj za prikaz
        sample = batch_data[:1]
        sample[:, :, 1:] = sample[:, :, 1:] / 10000.0
        
        pred = model(sample)
        gt = sample[0, 4] # Ground truth
        
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))
        axes[0].imshow(gt[0].cpu().numpy(), cmap='RdYlGn') 
        axes[0].set_title("Stvarni NDVI (Target)")
        axes[1].imshow(pred[0, 0].cpu().numpy(), cmap='RdYlGn')
        axes[1].set_title(f"Predikcija NDVI (E{epoch})")
        
        plt.savefig(MODELS_DIR / f"viz_epoch_{epoch}.png")
        plt.close()

class MasterBatchDataset(Dataset):
    def __init__(self, folder): self.files = list(Path(folder).glob("*.npz"))
    def __len__(self): return len(self.files)
    def __getitem__(self, idx): return torch.from_numpy(np.load(self.files[idx])['data']).float()

# --- TRENING PETLJA ---
def train():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    full_dataset = MasterBatchDataset(BATCH_DIR)
    train_size = int(0.8 * len(full_dataset))
    val_size = len(full_dataset) - train_size
    train_ds, val_ds = random_split(full_dataset, [train_size, val_size])

    train_loader = DataLoader(train_ds, batch_size=1, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=1)

    model = MasterUNet().to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()
    
    history = []
    best_val_loss = float('inf')
    epochs_without_improvement = 0

    logging.info(f"Start: Trening na {DEVICE}. Podaci: {len(full_dataset)} batcheva.")

    for epoch in range(1, EPOCHS + 1):
        model.train()
        t_loss = 0
        pbar = tqdm(train_loader, desc=f"Epoch {epoch}")
        
        for batch in pbar:
            batch = batch.squeeze(0).to(DEVICE)
            
            # NORMALIZACIJA NA LICU MJESTA
            # NDVI (kanal 0) ostaje, ostali se dijele s 10000
            batch_norm = batch.clone()
            batch_norm[:, :, 1:] = batch_norm[:, :, 1:] / 10000.0
            batch_norm = torch.nan_to_num(batch_norm, nan=0.0)
            
            target = batch_norm[:, 4] # Ciljna godina (2022 npr)
            
            optimizer.zero_grad()
            output = model(batch_norm)
            loss = criterion(output, target)
            loss.backward()
            
            # Gradient clipping protiv eksplozije gradijenata
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
            t_loss += loss.item()
            pbar.set_postfix({'loss': f"{loss.item():.6f}"})
        
        # VALIDACIJA
        model.eval()
        v_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                batch = batch.squeeze(0).to(DEVICE)
                batch[:, :, 1:] = batch[:, :, 1:] / 10000.0
                batch = torch.nan_to_num(batch, nan=0.0)
                v_loss += criterion(model(batch), batch[:, 4]).item()

        train_avg = t_loss / len(train_loader)
        val_avg = v_loss / len(val_loader)
        
        history.append({'epoch': epoch, 'train_loss': train_avg, 'val_loss': val_avg})
        logging.info(f"E{epoch} | Train: {train_avg:.6f} | Val: {val_avg:.6f}")

        # SPREMANJE
        pd.DataFrame(history).to_csv(LOG_CSV_PATH, index=False)
        save_plots(pd.DataFrame(history))
        
        if epoch % 2 == 0 or epoch == 1:
            visualize_prediction(epoch, model, batch)

        # EARLY STOPPING
        if val_avg < best_val_loss:
            best_val_loss = val_avg
            epochs_without_improvement = 0
            torch.save(model.state_dict(), MODEL_SAVE_PATH)
            logging.info("  -> Model spremljen.")
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= PATIENCE:
                logging.warning(f"STOP! Nema poboljšanja {PATIENCE} epoha.")
                break

if __name__ == "__main__":
    train()