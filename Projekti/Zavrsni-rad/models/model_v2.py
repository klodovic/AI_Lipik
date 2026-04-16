import torch
import torch.nn as nn

class ResBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.BatchNorm2d(channels), 
            nn.ReLU(),
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.BatchNorm2d(channels)
        )
    def forward(self, x): 
        return torch.relu(x + self.conv(x))

class MasterUNet(nn.Module):
    def __init__(self, in_channels=16, out_channels=4):
        super().__init__()
        # 16 ulaznih kanala jer tvoj forward radi reshape(B, 4*C, H, W) -> 4*4=16
        self.enc1 = nn.Sequential(nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.pool = nn.MaxPool2d(2)
        self.enc2 = nn.Sequential(nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.bottleneck = nn.Sequential(nn.Conv2d(64, 128, 3, padding=1), nn.ReLU())
        self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.dec2 = nn.Sequential(nn.Conv2d(128 + 64, 64, 3, padding=1), nn.ReLU(), ResBlock(64))
        self.dec1 = nn.Sequential(nn.Conv2d(64 + 32, 32, 3, padding=1), nn.ReLU(), ResBlock(32))
        self.final = nn.Sequential(nn.Conv2d(32, out_channels, 1), nn.Sigmoid())

    def forward(self, x):
        # x shape: [Batch, Sequence, Channels, Height, Width]
        B, S, C, H, W = x.shape
        # Uzimamo prve 4 godine sekvence i spajamo kanale (Flattening time into channels)
        x_in = x[:, :4].reshape(B, 4*C, H, W)
        
        e1 = self.enc1(x_in)
        e2 = self.enc2(self.pool(e1))
        b = self.bottleneck(self.pool(e2))
        
        d2 = self.dec2(torch.cat([self.up(b), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up(d2), e1], dim=1))
        
        return self.final(d1)