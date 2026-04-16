import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- KOPIRANA ARHITEKTURA MODELA (da ne moraš raditi import) ---
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
        x_in = x[:, :4].reshape(B, 4*C, H, W)
        e1 = self.enc1(x_in); e2 = self.enc2(self.pool(e1))
        b = self.bottleneck(self.pool(e2))
        d2 = self.dec2(torch.cat([self.up(b), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up(d2), e1], dim=1))
        return self.final(d1)

# --- OSTATAK SKRIPTE ZA PREDIKCIJU ---
BASE_DIR = Path("D:/copernicus-zagreb")
MODEL_PATH = BASE_DIR / "models/master_model_v2.pth"
TEST_BATCH = BASE_DIR / "data/batches_train/batch_0001.npz" 
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def predict():
    model = MasterUNet().to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()

    # Učitaj podatke
    data = np.load(TEST_BATCH)['data'] 
    sample = torch.from_numpy(data[2:3]).float().to(DEVICE) # Uzmi npr. 3. sekvencu u batchu
    
    # Normalizacija
    sample_norm = sample.clone()
    sample_norm[:, :, 1:] = sample_norm[:, :, 1:] / 10000.0
    
    with torch.no_grad():
        prediction = model(sample_norm)

    # Vizualizacija
    plt.figure(figsize=(15, 5))
    
    # 2026 stanje (Zadnji NDVI)
    plt.subplot(1, 3, 1)
    plt.imshow(sample[0, 4, 0].cpu(), cmap='RdYlGn')
    plt.title("Zadnje poznato stanje (2026)")
    
    # 2027 predikcija
    plt.subplot(1, 3, 2)
    plt.imshow(prediction[0, 0].cpu(), cmap='RdYlGn')
    plt.title("Model Predikcija (2027)")
    
    # Razlika
    plt.subplot(1, 3, 3)
    # Razlika između predviđenog 2027 i poznatog 2026
    diff = prediction[0, 0].cpu() - sample_norm[0, 4, 0].cpu()
    plt.imshow(diff, cmap='coolwarm', vmin=-0.2, vmax=0.2)
    plt.title("Detekcija promjena (2027 vs 2026)")
    plt.colorbar(label="NDVI razlika")
    
    plt.savefig(BASE_DIR / "models/final_prediction_2027.png")
    print(f"Predikcija spremljena u: {BASE_DIR}/models/final_prediction_2027.png")
    plt.show()

if __name__ == "__main__":
    predict()