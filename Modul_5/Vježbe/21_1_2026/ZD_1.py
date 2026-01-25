"""
Docstring for ZD_1

1. Zadatak - K-means clustering: segmentacija kupaca
Cilj
Cilj ovog zadatka je primijeniti algoritam K-means na stvarnom skupu podataka te upoznati osnovne korake nenadzirane segmentacije podataka, uključujući vizualnu analizu i odabir broja klastera pomoću elbow metode.
Skup podataka: Mall Customers
Koristite Mall Customers dataset koji sadrži informacije o kupcima trgovačkog centra.
U zadatku koristite sljedeće varijable:
● Annual Income (k$)
● Spending Score (1–100)
Dataset je pohranjen u CSV datoteci.
Zadatak
1. Učitavanje i priprema podataka
● Učitajte Mall Customers dataset iz CSV datoteke.
● Prikažite osnovne informacije o datasetu.
● Izdvojite varijable Annual Income (k$) i Spending Score (1–100) kao ulazne podatke.
2. Vizualna analiza podataka
● Nacrtajte scatter graf koji prikazuje odnos između godišnjeg prihoda i potrošačkog skora.
● Kratko opišite raspored podataka u prostoru značajki.
3. Odabir broja klastera (elbow metoda)
● Za vrijednosti broja klastera K od 1 do 10:
○ izgradite Pipeline koji se sastoji od:
■ StandardScaler
■ KMeans
○ istrenirajte model i zabilježite vrijednost inercije.
● Prikažite graf ovisnosti inercije o broju klastera.
● Na temelju grafa odaberite prikladnu vrijednost K.
4. K-means clustering
● Izgradite Pipeline s odabranim brojem klastera.
● Istrenirajte model i dohvatite:
○ oznake klastera za svaki uzorak
○ centre klastera.
● Centre klastera prikažite u originalnoj skali značajki.
5. Vizualizacija rezultata
● Prikažite podatke obojane prema pripadnosti klasterima.
● Označite centre klastera na grafu.
Kratka analiza
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Koju ste vrijednost K odabrali i zašto?
● Kako biste opisali dobivene klastere kupaca?
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Učitavanje podataka
df = pd.read_csv('Mall_Customers.csv')
print(df.info())

## Izdvanjanje varjabli
X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values


# 2. Vizualna analiza podataka
plt.scatter(X[:, 0], X[:, 1], s=20)
plt.title("Original data (no clustering)")
plt.show()

# 3. Odabir broja klastera (elbow metoda)
inertia_values = []
K_range = range(1, 11)

for K in K_range:
    pipeline = Pipeline(([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=K, random_state=42))
    ]))

    pipeline.fit(X)
    inertia_values.append(pipeline.named_steps['kmeans'].inertia_)

plt.plot(K_range, inertia_values, marker = 'o')
plt.title("Elbow method for optimal K")
plt.xlabel("Number of clusters K")
plt.ylabel("Inertia")
plt.xticks(K_range)
plt.show()

# Odabir K na temelju grafa
optimal_K = 5 # odabrano na temelju grafa

# 4. K-means clustering
pipeline = Pipeline(([
            ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=optimal_K, random_state=42))
]))

pipeline.fit(X)
labels = pipeline.named_steps['kmeans'].labels_
centers = pipeline.named_steps['kmeans'].cluster_centers_

# Pretvaranje centara natrag u originalnu skalu
scaler = pipeline.named_steps['scaler']
centers_original_scale = scaler.inverse_transform(centers)
print("Klusteri u originalnoj skali: \n", centers_original_scale)

# 5. Vizualizacija rezultata
plt.scatter(X[:, 0], X[:, 1], s=20, c=labels, cmap='viridis')
plt.scatter(centers_original_scale[:, 0], centers_original_scale[:, 1], s=100, c='red', marker='x', label='Centri klastera')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.title("K-means Clustering Results")
plt.show()


# Analiza
# ● Koju ste vrijednost K odabrali i zašto? 5 zbog Lakat metode koja pokazuje jasan pad inercije do te točke
# ● Kako biste opisali dobivene klastere kupaca? Klasteri predstavljaju različite skupine kupaca
# s obzirom na njihov godišnji prihod i potrošački score




























