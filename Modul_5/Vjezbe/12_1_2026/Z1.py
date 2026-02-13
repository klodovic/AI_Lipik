"""
Docstring for .ipynb_checkpoints.Vjezbe_2(12.1.2026)

1. Učitajte California Housing dataset kao Pandas DataFrame.
2. Grafički prikažite odnos svake ulazne varijable s ciljanom varijablom (target).
a. Koristite scatter grafove.
3. Na temelju grafičkog prikaza odaberite jednu ulaznu varijablu za koju smatrate da ima smislen linearan odnos s ciljem.
4. Podijelite podatke na train i test skup.
5. Istrenirajte model LinearRegression koristeći samo odabranu varijablu.
6. Izračunajte i ispišite metrike vrednovanja:
a. MSE
b. R²
7. Grafički prikažite:
a. test podatke
b. regresijsku liniju dobivenu modelom
Očekivanja
1. Kod mora biti reproducibilan (random_state)
2. Graf mora jasno pokazivati odnos između podataka i predikcije
3. U kratkom komentaru (1–2 rečenice) obrazložite zašto ste odabrali baš tu varijablu
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing


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

# 2. Grafički prikaz
visualize_data(X, y)

# 3. Odabir varijable
selected_feature = 'MedInc'
print("Odabrana znacajka:", selected_feature)
X_selected = X[[selected_feature]].values

# 4. Podjela podataka
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# 5. Treniranje modela
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 6. Izračunavanje metrika
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R²: {r2}")

# 7. Grafički prikaz rezultata
plt.scatter(X_test, y_test, color='blue', label='Test Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel(selected_feature)
plt.ylabel('Target')
plt.title("{}\nmse: {:.2f}\nr2: {:.2f}".format(selected_feature, mse, r2))
plt.legend()
plt.show()


# Komentar: varijabla 'MedInc' sam odabrao jer na grafičkom prikazu pokazuje jasan lineran odnos s ciljanom varijablom
