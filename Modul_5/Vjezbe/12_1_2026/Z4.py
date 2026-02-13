"""
Docstring for 12_1_2026.Z4

1. Odabir ulaznih varijabli
Koristite sljedeće ulazne varijable:
Numeričke varijable (skalirati):
● GrLivArea
● OverallQual
Kategoričke varijable (kodirati):
● Neighborhood
● HouseStyle
2. Priprema podataka
● Izdvojite odabrane ulazne varijable i ciljanu varijablu SalePrice.
● Podijelite podatke na train i test skup.
● Numeričke varijable:
○ skalirajte pomoću StandardScaler.
● Kategoričke varijable:
○ kodirajte pomoću OneHotEncoder.
(Napomena: numeričke i kategoričke varijable obrađujte odvojeno.)
3. Model
● Spojite skalirane numeričke i one-hot kodirane kategoričke varijable u jednu ulaznu matricu.
● Istrenirajte model LinearRegression.
● Izračunajte i ispišite metrike vrednovanja na test skupu:
○ MSE
○ R²
4. Kratka analiza
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Kako se promijenila dimenzionalnost ulaznih podataka nakon one-hot kodiranja?
● Je li model koji koristi i kategoričke varijable bolji od modela koji koristi samo numeričke varijable?
"""


import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import fetch_openml

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


# Učitavanje podataka
data = fetch_openml("house_prices", version=1, as_frame=True)
df = data.frame

# 1. Odabir ulaznih varijabli
selected_features = ["GrLivArea", "OverallQual", "Neighborhood", "HouseStyle"]
X = df[selected_features]
y = df["SalePrice"]

# 2. Priprema podataka
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Numeričke varijable
numerical_features = ["GrLivArea", "OverallQual"]
scaler = StandardScaler()
X_train_num = scaler.fit_transform(X_train[numerical_features])
X_test_num = scaler.transform(X_test[numerical_features])


# Kategoričke varijable
categorical_features = ["Neighborhood", "HouseStyle"]
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_train_cat = encoder.fit_transform(X_train[categorical_features])
X_test_cat = encoder.transform(X_test[categorical_features])

# 3. Spajanje podataka
X_train_prepared = np.hstack((X_train_num, X_train_cat))
X_test_prepared = np.hstack((X_test_num, X_test_cat))

# Trening modela
model = LinearRegression()
model.fit(X_train_prepared, y_train)
y_pred = model.predict(X_test_prepared)


# Metrika
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R²: {r2}")

# 4. Komentar
# Kako se promijenila dimenzionalnost ulaznih podataka nakon one-hot kodiranja? Povećao se broj značajki zbog one-hot 
# Je li model koji koristi i kategoričke varijable bolji od modela koji koristi samo numeričke varijable? 
# Da jer model koristi više informacija iz dataseta.

