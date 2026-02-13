"""
Docstring for ZD_3

3. Zadatak - PCA: redukcija dimenzionalnosti i rekonstrukcija lica
Cilj
Cilj ovog zadatka je upoznati se s metodom PCA (Principal Component Analysis) na primjeru slikovnog skupa podataka te razumjeti kako PCA može:
● smanjiti dimenzionalnost podataka (kompresija),
● sačuvati najvažnije informacije,
● omogućiti rekonstrukciju podataka iz smanjenog prostora.
Napomena: Dijelovi zadatka i odgovarajuće funkcije (npr. PCA.fit, transform, inverse_transform, components_, explained_variance_ratio_) bit će detaljno objašnjeni u prezentaciji ovih vježbi.
Skup podataka: Olivetti Faces
Koristite Olivetti faces dataset iz sklearn.datasets. Svaka slika je dimenzije 64 × 64, a u datasetu je predstavljena kao vektor duljine 4096 (svaki piksel je jedna značajka).
Zadatak
1. Učitavanje i osnovni pregled podataka
● Učitajte Olivetti faces dataset.
● Ispišite:
○ broj uzoraka (slika)
○ broj značajki (pikseli po slici)
● Prikažite nekoliko slika iz dataseta (npr. prvih 15) kako biste stekli dojam o podacima.
2. PCA model
● Postavite broj glavnih komponenti na 200.
● Inicijalizirajte PCA model i istrenirajte ga nad podacima.
● Ispišite dimenzije matrice komponenti (components_) i interpretirajte što te dimenzije znače u kontekstu slika.
3. Srednje lice (mean face)
● Prikažite mean face (prosječnu sliku) dobivenu iz PCA modela.
● Kratko objasnite što predstavlja ova slika.
4. Objašnjena varijanca
● Izračunajte kumulativnu objašnjenu varijancu (cumsum nad explained_variance_ratio_).
● Nacrtajte graf:
○ objašnjena varijanca po komponenti
○ kumulativna objašnjena varijanca
● Na temelju grafa procijenite koliko informacija otprilike zadržava prvih 200 komponenti.
5. Projekcija i rekonstrukcija
● Projicirajte podatke u PCA prostor pomoću transform.
● Rekonstruirajte slike natrag u originalni prostor pomoću inverse_transform.
● Prikažite jednu sliku:
○ original
○ rekonstruiranu (nakon PCA kompresije)
6. Vizualizacija komponenti (eigenfaces)
● Prikažite prve 4 PCA komponente kao slike (reshape na 64×64).
● Kratko komentirajte što primjećujete (npr. koje uzorke komponente “hvataju”).
Kratka analiza
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Što se vizualno mijenja na slici nakon rekonstrukcije pomoću PCA?
● Koju ulogu ima broj komponenti u kvaliteti rekonstrukcije?
● Što predstavljaju PCA komponente kada ih prikažemo kao slike?
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA

# 1. Učitavanje podataka
X_faces, y_id = fetch_olivetti_faces(return_X_y=True, shuffle=True,random_state=1)
num_images, num_pixels = X_faces.shape
print(f"Number of images: {num_images}, Number of pixels: {num_pixels}")

# Prikaz prvih 15 slika iz dataseta
fig, axes = plt.subplots(3,5, figsize = (10,6))
for i in range(15):
    axes[i//5, i%5].imshow(X_faces[i].reshape(64,64), cmap='gray')
    axes[i//5, i%5].axis('off')
plt.show()


# 2. PCA model
pca = PCA(n_components=200)
pca.fit(X_faces)
print(f"Dimenzije matrice komponenti: {pca.n_components_}")
# 

# 3. Srednje lice
mean_face = pca.mean_
plt.imshow(mean_face.reshape(64, 64), cmap="gray")
plt.axis("off")
plt.show()


# 4. Varijanca 
var_ratio = pca.explained_variance_ratio_
cum_var = np.cumsum(var_ratio)

## graf
plt.bar(range(len(var_ratio)), var_ratio)
plt.step(range(len(var_ratio)), cum_var)
plt.grid()
plt.show()

# 5. Projekcija i rekonstrukcija
Z = pca.transform(X_faces)
print(Z.shape) # svaka slike ja sada opisana sa 200 brojeva

X_reconstructed = pca.inverse_transform(Z)
print(X_reconstructed.shape) # vraćeno u originalni prostor

# prikaz originalne u rekonstruirane slike
index = 0
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(X_faces[index].reshape(64,64), cmap='gray')
plt.title("Originalna slika")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(X_reconstructed[index].reshape(64,64), cmap='gray')
plt.title("Rekonstruirana slika")
plt.axis('off')

plt.show()

# 6. Vizualizacija komponenti
fig, axes = plt.subplots(2,2, figsize=(8,8))
for i in range(4):
    axes[i//2, i%2].imshow(pca.components_[i].reshape(64,64), cmap='gray')
    axes[i//2, i%2].axis('off')
plt.show()

# Analiza
# ● Što se vizualno mijenja na slici nakon rekonstrukcije pomoću PCA? Slika gubi detalje i postaje zamućena
# ● Koju ulogu ima broj komponenti u kvaliteti rekonstrukcije? Veći broj komponenti rezultira boljom kvalitetom rekonstruirane slike
# ● Što predstavljaju PCA komponente kada ih prikažemo kao slike? Osnovene uzorke lica: sjena, obris lica, oči, naočale, usta, nos itd


