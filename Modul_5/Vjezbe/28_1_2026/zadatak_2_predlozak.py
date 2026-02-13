import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ============================================================
# KONFIGURACIJA (parametri kao "konstante" na vrhu datoteke)
# ============================================================

RANDOM_STATE = 1
RNG = np.random.default_rng(RANDOM_STATE)

# Dataset (1D regresija: nelinearna funkcija + šum)
N_SAMPLES = 2000
X_RANGE = (-3.0, 3.0)
NOISE_STD = 0.25
TEST_SIZE = 0.25

# MLP parametri
HIDDEN_LAYER_SIZES = (150, 100, 50)
ACTIVATION = "relu"
SOLVER = "sgd"
LEARNING_RATE_INIT = 0.01
EARLY_STOPPING = True
N_ITER_NO_CHANGE = 5
MAX_ITER = 100
VERBOSE = True
BATCH_SIZE='auto'
LEARNING_RATE = 'adaptive'

# Vizualizacija
LINE_POINTS = 800  # gustoća linije predikcije (veće = glađe)

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



def generate_nonlinear_1d_regression(n_samples, x_range, noise_std, rng):
    """
    Generira 1D regresijski dataset: y = sin(x)*x + 0.3*x^2 + šum
    X shape: (n_samples, 1)
    y shape: (n_samples,)
    """
    x = rng.uniform(x_range[0], x_range[1], size=n_samples)
    y_clean = np.sin(x) * x + 0.3 * (x ** 2)
    y = y_clean + rng.normal(0.0, noise_std, size=n_samples)
    X = x.reshape(-1, 1)
    return X, y, y_clean


def plot_regression_fit(X, y, model, title="MLPRegressor: predikcija"):
    """
    Crta scatter podataka i glatku krivulju predikcije modela (1D).
    """
    x_min, x_max = X.min(), X.max()
    x_line = np.linspace(x_min, x_max, LINE_POINTS).reshape(-1, 1)
    y_line = model.predict(x_line)

    plt.figure()
    plt.scatter(X[:, 0], y, s=18, alpha=0.35, edgecolor="k")
    plt.plot(x_line[:, 0], y_line, linewidth=2)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()


# ============================================================
# 1) GENERIRANJE PODATAKA
# ============================================================

X, y, y_clean = generate_nonlinear_1d_regression(
    n_samples=N_SAMPLES,
    x_range=X_RANGE,
    noise_std=NOISE_STD,
    rng=RNG
)

plt.figure()
plt.scatter(X[:, 0], y, s=18, alpha=0.35, edgecolor="k")
plt.title("Ulazni podaci (1D regresija, nelinearno + šum)")
plt.xlabel("X")
plt.ylabel("y")
plt.tight_layout()
plt.show()


# ============================================================
# 2) PODJELA NA TRAIN / TEST
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
)


# ============================================================
# 3) MODEL: PIPELINE (SCALER + MLPRegressor)
# ============================================================
clf = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("mlp", MLPRegressor(
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
mlp = clf.named_steps["mlp"]
print("\n--- INFO NAKON fit() ---")
print(f"n_iter_ = {mlp.n_iter_}")
print(f"n_layers_ = {mlp.n_layers_}")
print(f"out_activation_ = {mlp.out_activation_}")



# ============================================================
# 5) PREDIKCIJA I VREDNOVANJE
# ============================================================

y_pred = clf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\n--- REZULTATI NA TEST SKUPU ---")
print(f"MSE = {mse:.4f}")
print(f"R2  = {r2:.4f}")



# ============================================================
# 6) VIZUALIZACIJA: FIT KAO FUNKCIJA (1D)
# ============================================================
plot_regression_fit(X, y, clf, title="MLPRegressor: predikcija")


# ============================================================
# 8) loss_curve_ (dijagnostika učenja)
# ============================================================
mlp = clf.named_steps["mlp"]
plt.figure()
plt.plot(mlp.loss_curve_, label="loss_curve_")
plt.title("MLPRegressor: loss_curve_ tijekom treniranja")
plt.xlabel("Iteracija")
plt.ylabel("Vrijednost funkcije gubitka")
plt.legend()
plt.tight_layout()
plt.show()




