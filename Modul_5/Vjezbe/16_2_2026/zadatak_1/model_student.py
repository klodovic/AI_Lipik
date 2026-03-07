"""

1. Zadatak - Implementacija vlastite konvolucijske neuronske 
mreže (MNIST) 
U ovom zadatku implementirat ćete konvolucijsku neuronsku mrežu (CNN) za klasifikaciju 
znamenki iz MNIST dataseta. 
 
Arhitektura mreže prikazana je na slici student_CNN.png. 
Vaš zadatak je implementirati tu arhitekturu točno prema prikazanoj strukturi. 
1) Implementacija mreže (model_student.py) 
U datoteci model_student.py nalazi se template klase StudentCNN. 
Potrebno je: 
●  definirati konvolucijski dio mreže (Conv → ReLU → MaxPool) 
●  izračunati točan broj ulaznih značajki za prvi Linear sloj 
●  definirati potpuno povezani (fully connected) dio 
●  implementirati forward metodu 
Mreža mora odgovarati arhitekturi sa slike. 
Izlazni tensor mora imati oblik: 
[B, 10] 
gdje je: 
●  B - veličina batcha 
●  10 - broj klasa (znamenke 0-9) 
2) Konstrukcija modela (train.py) 
U skripti train.py nalazi se infrastruktura za: 
●  učitavanje MNIST dataseta 
●  podjelu na train i validacijski skup (90% / 10%) 
●  DataLoader-e 
●  trening petlju 
●  validacijsku petlju 
●  logiranje na TensorBoard 
U označenom TODO dijelu potrebno je: 
●  uvesti klasu StudentCNN 
●  konstruirati model s odgovarajućim parametrima 
●  prebaciti model na odgovarajući uređaj (CPU/GPU) 
3) Što radi train.py skripta? 
Skripta: 
1.  Loada MNIST dataset 
2.  Dijeli podatke na train i validation skup 
3.  Kreira DataLoader-e 
4.  Instancira model 
5.  Trenira model kroz zadani broj epoha 
6.  U trening petlji logira loss 
7.  U validacijskoj petlji logira accuracy 
Cilj je da model postigne visoku validacijsku točnost (≥ 97%). 
Važno 
●  Ne mijenjati strukturu train.py skripte. 
●  Implementacija mreže mora biti u model_student.py.

"""


import torch
import torch.nn as nn

    
class StudentCNN(nn.Module):
    def __init__(self, num_classes: int, in_channels: int = 1):
        """
        Konstruktor modela.

        Ovdje se definiraju svi slojevi mreže (npr. konvolucijski,
        aktivacijski, pooling i linearni slojevi) te se spremaju
        kao atributi klase.
        """
        super().__init__()

        # Konvolucijski slojevi
        self.features = nn.Sequential(
            nn.Conv2d(in_channels, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        # Fully connected slojevi
        self.classifier = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
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
