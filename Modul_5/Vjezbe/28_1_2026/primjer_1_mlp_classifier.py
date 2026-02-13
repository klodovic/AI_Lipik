import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

# ============================================================
# KONFIGURACIJA (parametri kao "konstante" na vrhu datoteke)
# ============================================================

RANDOM_STATE = 1

# Dataset
N_SAMPLES = 10000
NOISE = 0.25
TEST_SIZE = 0.25

# MLP parametri
HIDDEN_LAYER_SIZES = (150,150) #
ACTIVATION = "relu"
SOLVER = "sgd"
LEARNING_RATE = 'adaptive' #
LEARNING_RATE_INIT = 0.01 #
EARLY_STOPPING = True
N_ITER_NO_CHANGE = 10
MAX_ITER = 200 #
VERBOSE = True
BATCH_SIZE='auto'


# Vizualizacija decision boundary
GRID_STEP = 0.02  # manji = finija granica (sporije)

# ============================================================
# POMOĆNE FUNKCIJE
# ============================================================

def plot_decision_boundary_proba(model, X, y, title="Decision boundary (proba)"):
    """
    Crta decision boundary za 2D klasifikator koristeći predict_proba().
    - Pozadina: vjerojatnost klase 1 (glatko).
    - Linija: granica odluke na pragu 0.5.
    Pretpostavka: X ima shape (n_samples, 2).
    """
    x_min, x_max = X[:, 0].min() - 0.8, X[:, 0].max() + 0.8
    y_min, y_max = X[:, 1].min() - 0.8, X[:, 1].max() + 0.8

    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, GRID_STEP),
        np.arange(y_min, y_max, GRID_STEP),
    )

    grid = np.c_[xx.ravel(), yy.ravel()]

    # Vjerojatnost klase 1 (kolona 1), pa reshape u grid
    proba_class1 = model.predict_proba(grid)[:, 1].reshape(xx.shape)

    plt.figure()
    # Glatka pozadina: vjerojatnost (0..1)
    plt.contourf(xx, yy, proba_class1, levels=25, alpha=0.30)

    # Jasna granica odluke (p=0.5)
    plt.contour(xx, yy, proba_class1, levels=[0.5], colors="red", linewidths=2)

    # Podaci iznad svega
    plt.scatter(X[:, 0], X[:, 1], c=y, s=25, edgecolor="k", alpha=0.35)

    plt.title(title)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.tight_layout()
    plt.show()


# ============================================================
# 1) GENERIRANJE PODATAKA
# ============================================================

X, y = make_moons(n_samples=N_SAMPLES, noise=NOISE, random_state=RANDOM_STATE)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=25, alpha=0.35)
plt.title("make_moons: ulazni podaci (2 klase)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.tight_layout()
plt.show()

# ============================================================
# 2) PODJELA NA TRAIN / TEST
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

# ============================================================
# 3) MODEL: PIPELINE (SCALER + MLPClassifier)
# ============================================================

clf = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("mlp", MLPClassifier(
            hidden_layer_sizes=HIDDEN_LAYER_SIZES,
            activation=ACTIVATION,
            solver=SOLVER,
            batch_size=BATCH_SIZE,
            learning_rate=LEARNING_RATE,
            learning_rate_init=LEARNING_RATE_INIT,
            early_stopping=EARLY_STOPPING,
            n_iter_no_change=N_ITER_NO_CHANGE,
            max_iter=MAX_ITER,
            verbose=VERBOSE,
            random_state=RANDOM_STATE,
        )),
    ]
)

# ============================================================
# 4) TRENIRANJE
# ============================================================

clf.fit(X_train, y_train)

# pristup MLP objektu unutar pipeline-a
mlp = clf.named_steps["mlp"]
print("\n--- INFO NAKON fit() ---")
print(f"n_iter_ = {mlp.n_iter_}")
print(f"n_layers_ = {mlp.n_layers_}")
print(f"out_activation_ = {mlp.out_activation_}")


# ============================================================
# 5) PREDIKCIJA I VREDNOVANJE
# ============================================================

y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("\n--- REZULTATI NA TEST SKUPU ---")
print(f"Accuracy = {acc:.4f}")

print("\n--- classification_report ---")
print(classification_report(y_test, y_pred))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Matrica zabune (test)")
plt.tight_layout()
plt.show()

# ============================================================
# 6) DECISION BOUNDARY (na cijelom skupu za vizualni dojam)
# ============================================================

plot_decision_boundary_proba(
    clf, X, y,
    title="MLPClassifier decision boundary (make_moons, proba)"
)

# ============================================================
# 7) loss_curve_ (dijagnostika učenja)
# ============================================================

plt.figure()
plt.plot(mlp.loss_curve_)
plt.title("loss_curve_ (tijek učenja)")
plt.xlabel("Iteracija")
plt.ylabel("Gubitak")
plt.tight_layout()
plt.show()
