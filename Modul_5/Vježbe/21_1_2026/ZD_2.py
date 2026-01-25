"""
Docstring for ZD_2

2. Zadatak - K-means clustering: kompresija slike
Cilj
Cilj ovog zadatka je primijeniti algoritam K-means na slikovne podatke te pokazati kako se isti algoritam može koristiti u potpuno drugačijem kontekstu – za aproksimaciju i kompresiju slike. Naglasak je na razumijevanju reprezentacije slike kao skupa numeričkih vektora i vizualnoj interpretaciji rezultata.
Skup podataka
Koristite slikovnu datoteku (traffic_sign.png).
Slika je učitana pomoću OpenCV biblioteke i predstavlja se u RGB prostoru boja.
Zadatak
1. Učitavanje i prikaz slike
● Učitajte sliku pomoću OpenCV-a.
● Pretvorite sliku iz BGR u RGB prostor boja.
● Prikažite originalnu sliku.
2. Priprema podataka
● Odredite dimenzije slike.
● Pripremite podatke za K-means tako da:
○ svaki piksel predstavlja jedan uzorak
○ svaka boja (R, G, B) predstavlja značajku.
● Oblikujte podatke u odgovarajući oblik za učenje modela.
3. K-means clustering
● Istrenirajte K-means model s K = 16 klastera.
● Svakom pikselu pridružite najbliži centroid (boju).
● Dobivene centroide koristite za rekonstrukciju slike.
4. Rekonstrukcija i prikaz slike
● Rekonstruirajte sliku korištenjem centara klastera.
● Pripazite da su vrijednosti boja u ispravnom rasponu za prikaz.
● Prikažite:
○ originalnu sliku
○ komprimiranu sliku dobivenu K-means algoritmom.
Kratka analiza
U nekoliko rečenica odgovorite na sljedeća pitanja:
● Što se događa s izgledom slike nakon kompresije?
● Koju ulogu ima broj klastera K u kvaliteti rezultata?
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Učitavanje slike
image  = cv2.imread('traffic_sign.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.title("Original image")
plt.show()

# 2. Priprema podataka
rows, cols, ch = image.shape
pixels = image.reshape(rows * cols, ch)

# 3. K-means clustering
k = 16
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(pixels)
labels = kmeans.labels_
centers = kmeans.cluster_centers_.astype('uint8')

# Rekonstrukcija slike
compressed_image = centers[labels].reshape(rows, cols, ch)

# 4. Prikaz slike
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Originalana slika")
plt.subplot(1,2,2)
plt.imshow(compressed_image)
plt.title("Komprimirna slika K-means (k=16)")
plt.show()

# Analiza
# ● Što se događa s izgledom slike nakon kompresije? Slika gubi neke detalje i poprima cartoonish izgled
# ● Koju ulogu ima broj klastera K u kvaliteti rezultata? Veći broj klastera K rezultira boljom kvalitetom rekonstruirane slike
# 










