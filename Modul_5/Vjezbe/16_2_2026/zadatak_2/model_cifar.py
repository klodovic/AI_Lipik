
"""
2. Zadatak - Implementacija konvolucijske neuronske mreže 
(CIFAR-10) 
 
U ovom zadatku implementirat ćete konvolucijsku neuronsku mrežu (CNN) za klasifikaciju slika 
iz CIFAR-10 dataseta. 
Arhitektura mreže prikazana je na slici CIFAR_CNN.png. 
Vaš zadatak je implementirati tu arhitekturu točno prema prikazanoj strukturi. 
1) Implementacija mreže (model_cifar.py) 
U datoteci model_cifar.py nalazi se template klase CifarCNN. 
Potrebno je: 
●  definirati konvolucijski dio mreže (Conv → ReLU → MaxPool) 
●  pravilno pratiti promjenu dimenzija kroz tri konvolucijska bloka 
●  izračunati točan broj ulaznih značajki za prvi Linear sloj 
●  definirati potpuno povezani (fully connected) dio 
●  implementirati forward metodu  
Mreža mora odgovarati arhitekturi sa slike. 
Ulazni tensor ima oblik: [B, 3, 32, 32] 
Nakon trećeg pooling sloja izlaz mora biti: [B, 128, 4, 4] 
Flatten dimenzija mora iznositi: 2048 
Izlazni tensor mora imati oblik: [B, 10] 
gdje je: 
●  B – veličina batcha 
●  10 – broj klasa (CIFAR-10) 
2) Konstrukcija modela (train_cifar.py) 
U skripti train_cifar.py nalazi se infrastruktura za: 
●  učitavanje CIFAR-10 dataseta 
●  podjelu na train i validacijski skup (90% / 10%) 
●  DataLoader-e 
●  trening petlju 
●  validacijsku petlju 
●  logiranje na TensorBoard 
U označenom TODO dijelu potrebno je: 
●  uvesti klasu CifarCNN 
●  konstruirati model s odgovarajućim parametrima 
●  prebaciti model na odgovarajući uređaj (CPU/GPU) 
3) Što radi train_cifar.py skripta? 
 
Skripta: 
●  Loada CIFAR-10 dataset 
●  Dijeli podatke na train i validation skup 
●  Kreira DataLoader-e 
●  Instancira model 
●  Trenira model kroz zadani broj epoha 
●  U trening petlji logira loss 
●  U validacijskoj petlji logira accuracy  
Cilj je da model postigne stabilnu validacijsku točnost na CIFAR-10 datasetu. 
Važno 
Ne mijenjati strukturu train_cifar.py skripte. 
Implementacija mreže mora biti u model_cifar.py. 
"""

import torch
import torch.nn as nn

    
class CifarCNN(nn.Module):
    def __init__(self, num_classes: int, in_channels: int = 3):
        """
        Konstruktor modela.

        Ovdje se definiraju svi slojevi mreže (npr. konvolucijski,
        aktivacijski, pooling i linearni slojevi) te se spremaju
        kao atributi klase.
        """
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(in_channels, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.classifier = nn.Sequential(
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(),
            nn.Linear(256, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Definira tok podataka kroz mrežu.

        Ulazni tensor prolazi kroz prethodno definirane slojeve,
        a metoda vraća izlaz modela (logits).
        """
        x = self.features(x)
        x = torch.flatten(x, start_dim=1)  # Flatten za linearne slojeve
        x = self.classifier(x)

        return x
