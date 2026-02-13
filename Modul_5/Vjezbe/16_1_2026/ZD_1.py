"""
Docstring for 16_1_2026.ZD_1

1. Istraživanje podataka (vizualna analiza)
● Prikažite osnovne informacije o datasetu (broj uzoraka, distribucija klasa).
● Napravite scatter grafove za sve parove ulaznih varijabli:
○ variance
○ skewness
○ curtosis
○ entropy
● Točke na grafovima obojite prema klasi (class).
Na temelju grafova procijenite:
● koji par varijabli najbolje razdvaja klase
● gdje bi imalo smisla povući približno linearnu granicu razdvajanja
2. Odabir ulaznih varijabli
● Odaberite dvije ulazne varijable koje smatrate najprikladnijima za klasifikaciju pomoću logističke regresije.
● Kratko obrazložite svoj odabir.
3. Treniranje modela
● Izdvojite odabrane dvije varijable kao ulazne podatke.
● Podijelite dataset na train i test skup.
● Istrenirajte model LogisticRegression.
● Preporuka: skalirajte ulazne varijable prije treniranja (npr. pomoću StandardScaler).
4. Vrednovanje modela
Na test skupu izračunajte i prikažite:
● accuracy
● confusion matrix
● classification report (precision, recall, f1-score)
5. Vizualizacija rezultata
● Grafički prikažite decision boundary logističke regresije za odabrane dvije varijable.
● Usporedite decision boundary na:
○ train skupu
○ test skupu
Kratka analiza
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Koje ste dvije varijable odabrali i zašto?
● Kako izgleda decision boundary (linearna ili nelinearna granica)?
● Gdje model najčešće griješi (prema confusion matrici)?

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


# 1. IStraživanje podataka
print("Broj uzoraka:", df.shape[0])
print("Broj značajki:", df.shape[1])
print("Distribucija klasa:\n", df['class'].value_counts())

# Scatter plotovi
sns.pairplot(df, hue='class', vars=["variance", "skewness", "curtosis", "entropy"])
plt.suptitle("Scatter plotovi ulaznih varijabli", y=1.02)
plt.show()

# 2. Odabir ulaznih varijabli

## Odaberite dvije ulazne varijable koje smatrate najprikladnijima za klasifikaciju pomoću logističke regresije
selected_features = ["variance", "skewness"] # zbog Gaussian distribucije i dobre separacije klasa

# 3. Treniranje modela
X = df[selected_features].values
y = df['class'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('LogReg', LogisticRegression())
])

pipeline.fit(X_train, y_train)

# 4. Vrednovanje modela
y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
conf_martix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\nRezultati na test skupu:")
print(f"Accuracy: {acc:.3f}")
print("Confusion Matrix: \n", conf_martix)
print("Classification Report:\n", class_report)



# 5. Vizualizacija rezultata
plot_decision_boundary(pipeline, X_train, y_train, "Decision Boundary na train skupu")
plot_decision_boundary(pipeline, X_test, y_test, "Decision Boundary na test skupu")

disp = ConfusionMatrixDisplay(confusion_matrix=conf_martix, display_labels=pipeline.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()


# Analiza
# Koje se dvije varijable odobrale i zašto? 
# selected_features = ["variance", "skewness"] # zbog Gaussian distribucije i dobre separacije klasa

# Kako izgleda decision boundary (linearna ili nelinerana granica)?
# Decision boundary je linearna

# Gdje model najčešće griješi (prema confusion matrici)?
# Model najčešće griješi na pozitivnim uzorcima koji su klasificirani kao negativni


















