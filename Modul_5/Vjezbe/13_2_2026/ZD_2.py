import torch
import torch.nn as nn
from torchvision import transforms, models
from torchvision.models import ResNet18_Weights
from PIL import Image

# 1) DEVICE PROVJERA
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Koristi se device: {device}")


# 2) DEFINICIJA TRANSFORMACIJA
# (MORAJU biti iste kao u treniranju)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
])


# 3) KREIRANJE ISTE ARHITEKTURE
model = models.resnet18(weights=None)  # bez pretrained weights
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)


# 4) UČITAVANJE TEŽINA
model.load_state_dict(torch.load("resnet18_mnist.pth", map_location=device))
model = model.to(device)

# Postavljanje u eval mode
model.eval()

print("Model uspješno učitan.")


# 5) UČITAVANJE SLIKE
image_path = "nums/1.jpg"  
image = Image.open(image_path)

# Primjena transformacija
image = transform(image)

# Dodavanje batch dimenzije
image = image.unsqueeze(0)

image = image.to(device)

print(f"Oblik ulaza u model: {image.shape}")  # mora biti [1, 3, 224, 224]

# 6) INFERENCIJA
with torch.no_grad():
    outputs = model(image)
    _, predicted = torch.max(outputs, 1)

print(f"Predviđena znamenka: {predicted.item()}")
