"""
Docstring for 12_1_2026.Z3

1. Učitajte podatke iz datoteke nonlinear_data.npz.
2. Grafički prikažite podatke (scatter X vs y).
3. Podijelite podatke na train i test skup.
4. Za različite stupnjeve polinoma (degree):
○ npr. 1, 2, 3, 5, 7
○ transformirajte podatke pomoću PolynomialFeatures
○ istrenirajte model LinearRegression
5. Za svaki stupanj polinoma:
○ izračunajte MSE i R² na test skupu
○ grafički prikažite predikciju modela
6. Usporedite rezultate za različite stupnjeve polinoma.
Pitanja za razmišljanje (obavezno odgovoriti)
● Kako se ponaša model za mali stupanj polinoma?
● Što se događa kada je stupanj polinoma vrlo velik?
● Uočavate li pojavu overfittinga?
● Koji stupanj polinoma daje najbolju ravnotežu između:
○ kvalitete prilagodbe
○ generalizacije na test skupu?
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


def load_data(path: str = "nonlinear_data.npz"):
    data = np.load(path)
    X = data["X"]
    y = data["y"]
    return X, y


def plot_test_fit(X_test, y_test, y_pred, title: str):
    """
    Crta test točke + regresijski pravac.
    Sortiranje po X je važno da linija bude uredna (bez cik-cak spajanja).
    """
    idx = np.argsort(X_test[:, 0])
    X_sorted = X_test[idx]
    y_test_sorted = y_test[idx]
    y_pred_sorted = y_pred[idx]

    plt.figure(figsize=(8, 5))
    plt.scatter(X_sorted, y_test_sorted, color="black", alpha=0.5, s=10, label="Test podaci")
    plt.plot(X_sorted, y_pred_sorted, linewidth=3, label="Linearna regresija (pravac)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.show()


# 1. Učitavanje podataka
X, y = load_data("nonlinear_data.npz")

# 2 Prikaz sirovih podataka (sve točke)
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="black", alpha=0.35, s=10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Nelinearni podaci")
plt.show()

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 4. polinomial regression za različite stupnjeve

degrees = [1, 2, 3, 5, 20]
results = {}

for degree in degrees:
    # Transformacija podataka
    poly_transformer = PolynomialFeatures(degree=degree)
    X_train_poly = poly_transformer.fit_transform(X_train)
    X_test_poly = poly_transformer.transform(X_test)

    # Treniranje modela
    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    # Predikcija
    y_pred = model.predict(X_test_poly)

    # 5. Metrike
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[degree] = (mse, r2)

    # Grafički prikaz
    title = f"Polynomial Degree: {degree} | MSE: {mse:.2f}, R²: {r2:.2f}"
    plot_test_fit(X_test, y_test, y_pred, title)

# 6. Usportedba rezultata
print("Rezultati za različite stupnjeve polinoma:")
for degree, (mse, r2) in results.items():
    print(f"Degree: {degree} | MSE: {mse:.2f}, R²: {r2:.2f}")


# Komentar:
# Kako se ponaša model za mali stupanj polinoma? Model ne može dobro pratiti strukture podataka
# Što se događa kada je stupanj polinoma vrlo velik? Model se previše prilagođava treniranim podacima - overfitting
# Uočavate li pojavu overfittinga? Da, naročito kod zadnjeg stupnja (20)
# Koji stupanj polinoma daje najbolju ravnotežu između: Stupnjevi od 2 - 5 daju dobru ravnotežu
