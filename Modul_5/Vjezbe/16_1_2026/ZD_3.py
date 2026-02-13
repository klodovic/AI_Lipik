"""
Docstring for 16_1_2026.ZD_3

U ovom zadatku koristite sve ulazne varijable:
● variance
● skewness
● curtosis
● entropy
Ciljna varijabla je class (binarna klasifikacija).
Zadatak
1. Priprema podataka
○ Učitajte dataset.
○ Prikažite osnovne informacije o skupu podataka i distribuciju klasa.
○ Podijelite podatke na train i test skup.
2. Treniranje i usporedba modela Na istom train/test skupu istrenirajte sljedeće modele:
○ Logistička regresija
■ koristite sve ulazne varijable
■ po potrebi primijenite skaliranje značajki
○ KNN
■ isprobajte različite vrijednosti parametra k
■ obavezno koristite skaliranje značajki
○ Decision Tree
■ isprobajte različite vrijednosti parametra max_depth
3. Vrednovanje modela Za svaki model (i odabrane hiperparametre) na test skupu izračunajte i prikažite:
○ accuracy
○ confusion matrix
○ classification report
Analiza i interpretacija
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Koji je model postigao najbolji rezultat na test skupu?
● Kako su promjene hiperparametara utjecale na rezultate KNN-a i decision tree-a?
● Koji biste model odabrali za praktičnu primjenu i zašto?
Napomena
U ovom zadatku nije potrebno vizualizirati decision boundary, jer se koriste sve ulazne varijable (višedimenzionalni prostor).

"""



import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

import pandas as pd
import seaborn as sns


def plot_decision_boundary(model, X, y, title):
    """
    Iscrtava decision boundary za 2D podatke koristeći
    vjerojatnost pripadnosti klasi 1.
    """
    x_min, x_max = X[:, 0].min() - 1.0, X[:, 0].max() + 1.0
    y_min, y_max = X[:, 1].min() - 1.0, X[:, 1].max() + 1.0

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300),
    )

    grid = np.c_[xx.ravel(), yy.ravel()]
    probs = model.predict_proba(grid)[:, 1]
    probs = probs.reshape(xx.shape)

    plt.figure(figsize=(7, 6))
    plt.contourf(xx, yy, probs, levels=50, alpha=0.6)
    plt.colorbar(label="P(klasa = 1)")
    plt.contour(xx, yy, probs, levels=[0.5], linewidths=2)

    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", alpha=0.85)
    plt.xlabel("Značajka 1")
    plt.ylabel("Značajka 2")
    plt.title(title)
    plt.show()


# Učitavanje podataka
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/banknote_authentication.csv"

print(url)
df = pd.read_csv(url, header=None)
df.columns = ["variance", "skewness", "curtosis", "entropy", "class"]

# 1. Istraživanje podataka
print("Broj uzoraka:", df.shape[0])
print("Broj značajki:", df.shape[1])
print("Distribucija klasa:\n", df['class'].value_counts())

# Odabir svih značajki
selected_features = ["variance", "skewness", "curtosis", "entropy"]
X = df[selected_features].values
y = df['class'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)

# 2. Treniranje modela - Logistička reg
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(random_state=42))
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

#3. Vrednovanje modela
print("Logistička regresija:")
acc_logreg = accuracy_score(y_test, y_pred)
print(f"Točnost: {acc_logreg:.4f}")
conf_matrix_logreg = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix_logreg)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Treniranje modela - KNN
pipeline_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
pipeline_knn.fit(X_train, y_train)
y_pred_knn = pipeline_knn.predict(X_test)   
# Vrednovanje modela - KNN
print("KNN:")
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"Točnost: {acc_knn:.4f}")
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)
print("Confusion Matrix:\n", conf_matrix_knn)
print("Classification Report:\n", classification_report(y_test, y_pred_knn))

# Treniranje modela - Decision Tree
pipeline_dt = Pipeline([
    ('dt', DecisionTreeClassifier(max_depth=5, random_state=42))
])
pipeline_dt.fit(X_train, y_train)
y_pred_dt = pipeline_dt.predict(X_test)

# Vrednovanje modela - Decision Tree
print("Decision Tree:")
acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"Točnost: {acc_dt:.4f}")
conf_matrix_dt = confusion_matrix(y_test, y_pred_dt)
print("Confusion Matrix:\n", conf_matrix_dt)
print("Classification Report:\n", classification_report(y_test, y_pred_dt))
