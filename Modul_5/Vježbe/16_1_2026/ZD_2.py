"""
Docstring for 16_1_2026.ZD_2

Zadatak
1. Priprema podataka
● Učitajte originalni dataset.
● Na temelju ciljne varijable izradite izmijenjenu verziju dataseta u kojoj su klase neravnomjerno zastupljene, tako da zadržite sve uzorke jedne klase, a od druge klase zadržite otprilike 10 % uzoraka.
● Prikažite novu distribuciju klasa.
2. Odabir ulaznih varijabli
● Kao i u prethodnom zadatku, vizualno analizirajte odnose između ulaznih varijabli.
● Na temelju scatter grafova odaberite dvije ulazne varijable koje smatrate najprikladnijima za linearnu klasifikaciju.
● Kratko obrazložite svoj odabir.
3. Treniranje modela (osnovni model)
● Podijelite podatke na train i test skup.
● Istrenirajte model logističke regresije na izmijenjenom (neravnotežnom) skupu podataka.
● Po potrebi primijenite skaliranje ulaznih varijabli.
● Izračunajte i prikažite:
○ accuracy
○ confusion matrix
○ classification report
4. Vizualizacija rezultata
● Grafički prikažite decision boundary logističke regresije za odabrane dvije varijable.
● Obratite pažnju na ponašanje modela u području manjinske klase.
5. Ponovljeni eksperiment
● Ponovite cijeli postupak treniranja i vrednovanja modela, ali ovaj put iskoristite mogućnost uravnoteživanja utjecaja klasa tijekom učenja modela, bez promjene odabranih varijabli ili podjele na train i test skup.
● Nemojte mijenjati odabrane varijable niti način podjele na train i test skup.
Analiza i interpretacija
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Kako se promijenila distribucija predikcija između dva modela?
● Kako su se promijenile metrike za manjinsku klasu?
● Je li accuracy dobra mjera kvalitete modela u ovom slučaju?
● Koji biste model smatrali prikladnijim za praktičnu primjenu i zašto?

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
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

# Scatter plotovi
sns.pairplot(df, hue='class', vars=["variance", "skewness", "curtosis", "entropy"])
plt.suptitle("Scatter plotovi ulaznih varijabli", y=1.02)
plt.show()


# 2. Odabir ulaznih varijabli
selected_features = ["variance", "skewness"]
X = df[selected_features].values
y = df['class'].values
# Obrazloženje odabira:
# Odabrane su varijable "variance" i "skewness" jer najbolje razdvajaju klase na scatter plotovima, 
# što ukazuje na njihovu prikladnost za linearnu klasifikaciju.

# 3. Treniranje modela 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('LogReg', LogisticRegression())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
conf_martix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
print("\nRezultati na test skupu:")
print(f"Accuracy: {acc:.3f}")
print("Confusion Matrix: \n", conf_martix)
print("Classification Report:\n", class_report)


# 4. Vizualizacija rezultata
plot_decision_boundary(pipeline, X_train, y_train, "Decision Boundary na train skupu - Non Balanced")
plot_decision_boundary(pipeline, X_test, y_test, "Decision Boundary na test skupu - Non Balanced")

disp = ConfusionMatrixDisplay(confusion_matrix=conf_martix, display_labels=pipeline.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix (uravnoteženi model)")
plt.show()

# 5. Ponovljeni eksperiment s uravnoteženjem klasa
pipeline_balanced = Pipeline([
    ('scaler', StandardScaler()),
    ('LogReg', LogisticRegression(class_weight='balanced'))     
])

pipeline_balanced.fit(X_train, y_train)
y_pred_balanced = pipeline_balanced.predict(X_test)

acc_balanced = accuracy_score(y_test, y_pred_balanced)
conf_martix_balanced = confusion_matrix(y_test, y_pred_balanced)
class_report_balanced = classification_report(y_test, y_pred_balanced)

print("\nRezultati na test skupu (uravnoteženi model):")
print(f"Accuracy: {acc_balanced:.3f}")
print("Confusion Matrix: \n", conf_martix_balanced)
print("Classification Report:\n", class_report_balanced)

# Vizualizacija cm za uravnoteženi model
plot_decision_boundary(pipeline_balanced, X_train, y_train, "Decision Boundary na train skupu - Balanced")
plot_decision_boundary(pipeline_balanced, X_test, y_test, "Decision Boundary na test skupu - Balanced")

disp = ConfusionMatrixDisplay(confusion_matrix=conf_martix_balanced, display_labels=pipeline_balanced.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix (uravnoteženi model)")
plt.show()