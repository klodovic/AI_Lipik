"""
3. Zadatak - MLPRegressor: implementacija regresijskog modela neuronske mreže
Cilj
Cilj ovog zadatka je primijeniti potpuno povezanu neuronsku mrežu (MLPClassifier) na stvarni skup podataka s više klasa te provesti cjelokupan postupak višeklasne klasifikacije u scikit-learnu.
Naglasak je na:
● radu sa stvarnim podacima učitanima iz vanjskog izvora,
● pripremi podataka za učenje,
● implementaciji i treniranju MLP klasifikatora,
● interpretaciji rezultata višeklasne klasifikacije.
Skup podataka
U zadatku se koristi Dry Bean Dataset, preuzet s UCI Machine Learning Repositoryja.
Dataset sadrži:
● numeričke značajke dobivene iz slike zrna graha,
● više klasa koje predstavljaju različite vrste graha,
● stvarne, nelinearne podatke bez “toy” pojednostavljenja.
Podaci se učitavaju programski pomoću dostupne Python biblioteke.
Učitavanje skupa podataka
Dry Bean Dataset potrebno je učitati programski korištenjem dostupne Python biblioteke.
Na službenoj stranici dataseta nalaze se upute kako dataset preuzeti i učitati u Pythonu. Prije početka rada proučite taj dio dokumentacije i koristite preporučeni način učitavanja podataka.
Učitani podaci trebaju biti dostupni u obliku:
● pandas DataFrame-a za značajke,
● ciljne varijable koja odgovara višeklasnom problemu.
Važna napomena
Ciljna varijabla u ovom datasetu sadrži tekstualne oznake klasa.
Prije treniranja modela potrebno je koristiti LabelEncoder kako bi se klase ispravno pripremile za učenje neuronske mreže.
Detalji implementacije prepušteni su vama.
Zadatak
1. Upoznavanje s podacima
Analizirajte učitani skup podataka:
● provjerite dimenzije skupa podataka,
● promotrite raspodjelu klasa,
● razmotrite zašto je riječ o višeklasnom problemu.
2. Priprema podataka
Pripremite podatke za učenje:
● razdvojite značajke i ciljnu varijablu,
● osigurajte da su ulazni podaci numeričkog tipa,
● kodirajte ciljne klase pomoću LabelEncodera,
● podijelite podatke na train i test skup uz očuvanje raspodjele klasa.
3. Treniranje MLP klasifikatora
Istrenirajte MLPClassifier unutar Pipeline-a koji uključuje skaliranje podataka.
Nakon treniranja:
● ispišite osnovne informacije o modelu,
● provjerite broj iteracija i izlaznu aktivacijsku funkciju.
4. Vrednovanje višeklasnog modela
Evaluirajte model korištenjem:
● točnosti klasifikacije (accuracy),
● classification_reporta,
● matrice zabune (confusion matrix).
Obratite pažnju na:
● razlike u uspješnosti između pojedinih klasa,
● koje se klase najčešće međusobno miješaju.
"""


from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
dry_bean = fetch_ucirepo(id=602) 
  
# data (as pandas dataframes) 
X = dry_bean.data.features 
#y = dry_bean.data.targets 
y = dry_bean.data.targets.iloc[:, 0]
  
# metadata 
print(dry_bean.metadata) 
  
# variable information 
print(dry_bean.variables) 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay


# ============================================================
# KONFIGURACIJA (parametri kao "konstante" na vrhu datoteke)
# ============================================================

RANDOM_STATE = 1
TEST_SIZE = 0.25

# MLP parametri
HIDDEN_LAYER_SIZES = (150,100)
ACTIVATION = "relu"
SOLVER = "sgd"
LEARNING_RATE_INIT = 0.01
EARLY_STOPPING = True
N_ITER_NO_CHANGE = 10
MAX_ITER = 200
VERBOSE = True
BATCH_SIZE='auto'
LEARNING_RATE = 'adaptive'

# ============================================================

# 1) Podaci
print(f"Dimenzije skupa podataka: X={X.shape}, y={y.shape}")
print("Raspodjela klasa:")
print(y.value_counts()) 

print(dry_bean.data.targets['Class'].value_counts())
print("Ovo je višeklasni problem jer ciljna varijabla sadrži više od dvije klase.")



# 2) Priprema podataka
# Kodiranje ciljane varijable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Podijeliti podatke na train i test skup
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y_encoded)

# 3) Treniranje MLP klasifikatora unutar Pipeline-a
pipeline_steps = [
    ("scaler", StandardScaler()),
    (
        "mlp",
        MLPClassifier(
            hidden_layer_sizes=HIDDEN_LAYER_SIZES,
            activation=ACTIVATION,
            solver=SOLVER,
            learning_rate_init=LEARNING_RATE_INIT,
            early_stopping=EARLY_STOPPING,
            n_iter_no_change=N_ITER_NO_CHANGE,
            max_iter=MAX_ITER,
            verbose=VERBOSE,
            batch_size=BATCH_SIZE,
            learning_rate=LEARNING_RATE,
            random_state=RANDOM_STATE,
        ),
    ),
]

clf = Pipeline(steps=pipeline_steps)
clf.fit(X_train, y_train)
mlp = clf.named_steps["mlp"]
print("\n--- INFO NAKON fit() ---")
print(f"n_iter_ = {mlp.n_iter_}")
print(f"n_layers_ = {mlp.n_layers_}")
print(f"out_activation_ = {mlp.out_activation_}")

#4) Vredonovanje modela
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("\n--- REZULTATI NA TEST SKUPU ---")
print(f"Accuracy = {acc:.4f}")
print("\n--- classification_report ---")
print(classification_report(y_test, y_pred))

# Matrica zabune
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Matrica zabune (test)")
plt.show()

# =============================================================
# Dodane Vizaulizacije loss_curve_
mlp = clf.named_steps["mlp"]
plt.figure()    
plt.plot(mlp.loss_curve_)
plt.title("Loss Curve")
plt.xlabel("Iteracija")
plt.ylabel("Gubitak")
plt.show()



