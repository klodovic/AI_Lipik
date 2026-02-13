import torch 
from torch.utils.data import random_split
from torchvision import datasets, transforms
from torchvision.models import resnet18, ResNet18_Weights
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter


# 1) DEVICE PROVJERA
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Koristi se device: {device}")


# 2) TRANSFORMACIJE
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
])


# 3) DATASET
dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

train_size = int(0.9 * len(dataset))
val_size = len(dataset) - train_size


train_dataset, val_dateset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dateset, batch_size=64, shuffle=False)


# 4) Vizualizacija
for images, labels in train_loader:
    print(images.shape)
    break

# 5) Model
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)

# Zamjena zadnjeg sloja
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

# Zamrzavanje backbonea (opcionalno)
for param in model.parameters():
    param.requires_grad = False

for param in model.fc.parameters():
    param.requires_grad = True

model = model.to(device)


# 6) LOSS & OPTIMIZER
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)


# 7) TENSORBOARD
writer = SummaryWriter("runs/resnet18_mnist")


# 8) Trening
num_epochs = 5

for epoch in range(num_epochs):
    model.train()
    train_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_acc = correct / total
    train_loss /= len(train_loader)

    # ===== VALIDACIJA =====
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)

            val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    val_acc = correct / total
    val_loss /= len(val_loader)

    print(f"Epoch [{epoch+1}/{num_epochs}]")
    print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
    print(f"Val Loss:   {val_loss:.4f} | Val Acc:   {val_acc:.4f}")
    print("-" * 40)

    writer.add_scalar("Loss/Train", train_loss, epoch)
    writer.add_scalar("Loss/Validation", val_loss, epoch)
    writer.add_scalar("Accuracy/Train", train_acc, epoch)
    writer.add_scalar("Accuracy/Validation", val_acc, epoch)

# 9) SPREMANJE MODELA

torch.save(model.state_dict(), "resnet18_mnist.pth")
print("Model spremljen!")

writer.close()








