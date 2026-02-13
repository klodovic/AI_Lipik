"""
Docstring for 12_1_2026.Z2

1. Učitajte California Housing dataset.
2. Izračunajte i grafički prikažite korelacijsku matricu:
a. uključite sve ulazne varijable
b. uključite i ciljanu varijablu (target)
3. Na temelju korelacijske matrice:
a. odaberite dvije, tri ili više ulaznih varijabli
b. obrazložite zašto ste ih odabrali
4. Podijelite podatke na train i test skup.
5. Prije treniranja modela skalirajte ulazne varijable (npr. StandardScaler).
a. Skaliranje mora biti izvedeno ispravno (fit na train skupu).
6. Istrenirajte model LinearRegression.
7. Izračunajte i ispišite metrike vrednovanja:
a. MSE
b. R²
Očekivanja
1. Skaliranje mora biti dio rješenja
2. Usporedite dobivene metrike s rezultatom iz Zadatka 1
3. U kratkom komentaru odgovorite:
a. Je li model bolji?
b. Koje varijable imaju najveći utjecaj?
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

def plot_correlation_matrix(X_df, y):
    """
    Prikazuje korelacijsku matricu između:
    - svih ulaznih značajki
    - ciljne varijable (target)
    """

    corr_df = X_df.copy()
    corr_df["target"] = y

    corr_matrix = corr_df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )
    plt.title("Korelacijska matrica (ulazne značajke + cilj)")
    plt.show()

def analyze_single_feature_models(X_df, y):
    """
    Za svaku značajku:
    - trenira linearni regresijski model
    - računa MSE i R²
    - grafički prikazuje test podatke i regresijsku liniju
    """

    number_of_features = X_df.shape[1]
    n_cols = 5
    n_rows = number_of_features // n_cols
    if number_of_features % n_cols != 0:
        n_rows += 1

    fig = plt.figure()
    fig.suptitle("Linearna regresija - pojedinačne značajke", fontsize=14)

    for i, feature_name in enumerate(X_df.columns):
        X_feature = X_df[[feature_name]].values

        X_train, X_test, y_train, y_test = train_test_split(
            X_feature, y, test_size=0.2, random_state=1
        )

        model = linear_model.LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        ax = fig.add_subplot(n_rows, n_cols, i + 1)
        ax.scatter(X_test, y_test, color="black", s=10)
        ax.plot(X_test, y_pred, color="blue", linewidth=2)

        ax.set_title(
            f"{feature_name}\n"
            f"MSE: {mse:.1f}, R²: {r2:.2f}",
            fontsize=9
        )
        ax.set_xlabel(feature_name)
        ax.set_ylabel("Target")

    plt.subplots_adjust(
        left=0.05,
        right=0.98,
        top=0.90,
        bottom=0.07,
        wspace=0.35,
        hspace=0.5
    )
    plt.show()

def visualize_data(X, y):
    _, number_of_features = X.shape
    number_of_graph_columns = 5
    number_of_graph_rows = number_of_features // number_of_graph_columns
    if number_of_features % number_of_graph_columns != 0:
        number_of_graph_rows += 1

    fig = plt.figure()

    for i, feature_name in enumerate(X):
        ax = fig.add_subplot(number_of_graph_rows, number_of_graph_columns, i + 1)
        ax.scatter(X[feature_name], y)
        ax.set_title(feature_name)
        ax.set_xlabel(feature_name)
        ax.set_ylabel("Diabetes progression (target)")

    plt.subplots_adjust(left=0.058,
                        right=0.962,
                        top=0.88,
                        bottom=0.08,
                        wspace=0.35,
                        hspace=0.3)
    plt.show()


# 1. Učitajte California Housing dataset kao Pandas DataFrame.
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target


# 2. Izračunajte i grafički prikažite korelacijsku matricu
plot_correlation_matrix(X, y)


# 3. MedInc, AveRooms i AveOccup imaju najveću korelaciju s ciljanom varijablom (target)
selected_features = ['MedInc', 'AveRooms', 'AveOccup']
print("Odabrane značajke:", selected_features)


# 4. Podjela podataka
X_train, X_test, y_train, y_test = train_test_split(X[selected_features], y, test_size=0.2, random_state=42)


# 5. Skaliranje podataka
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 6. Treniranje modela
model = linear_model.LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# 7. Metrika
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R²: {r2}")

# Analiza modela s pojedinačnim značajkama
analyze_single_feature_models(X[selected_features], y)

# komentar:
# u prvom zadatku:  MSE: 0.7091157771765549  R²: 0.45885918903846656
# u drugom zadatku: MSE: 0.7006855912225249  R²: 0.4652924370503557 
# a. Je li model bolji?
# Da, model je neznatno bolji, vjerovatno zbog malog dataseta

# b. Koje varijable imaju najveći utjecaj?
# MedInc ima najveći utjecaj na model jer pokazuje najvišu korelaciju s ciljanom varijablom.
