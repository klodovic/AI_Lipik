import csv
from pathlib import Path

import torch
from torch.utils.data import Dataset
from PIL import Image


class PetsCsvDataset(Dataset):

    def __init__(self, csv_path, images_dir, transform=None):
        self.csv_path = Path(csv_path)
        self.images_dir = Path(images_dir)
        self.transform = transform

        self.samples = []
        labels = []

        with open(self.csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header

            for row in reader:
                filename, label_str = row
                labels.append(label_str)
                self.samples.append((filename, label_str))

        # ===== AUTOMATSKO MAPIRANJE KLASA =====
        self.classes = sorted(set(labels))
        self.class_to_idx = {cls: i for i, cls in enumerate(self.classes)}

        # pretvori label string -> index
        self.samples = [
            (fname, self.class_to_idx[label])
            for fname, label in self.samples
        ]

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_name, label = self.samples[idx]

        img_path = self.images_dir / img_name
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, torch.tensor(label, dtype=torch.long)