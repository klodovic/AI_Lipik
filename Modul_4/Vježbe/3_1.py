import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
1.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji.
a)
Pretvori sliku u boji u sliku sa sivim tonovima.
b)
Izračunaj histogram slike u sivim tonovima i prikaži ga pomoću matplotlib biblioteke. Komentiraj dobiveni rezultat.
c)
Izračunaj histogram za svaki kanal slike; pri crtanju histograma koristi različite boje za svaki kanal.
d)
Modificirajte kod za prikaz
"""

#img = cv2.imread("3_1/primjer_1.png")

slika = cv2.imread('img/primjer_1.png', cv2.IMREAD_GRAYSCALE)

# plt.figure(figsize=(10,5))
# plt.imshow(slika, cmap='gray')
# plt.title("Slika u sivim tonovima")
# plt.show()

hist_sivi, bins = np.histogram(slika, 256, [0,256])
plt.figure(figsize=(10,5))
plt.plot(hist_sivi, color='black')
plt.title("Histogram slike u sivim tonovima")
plt.xlabel("Intenzitet piksela")
plt.ylabel("Broj piksela")
plt.xlim([0,256])
plt.show()
# Komentar: Histogram pokazuje raspodjelu intenziteta piksela u slici. Visoke vrijednosti na određenim intenzitetima 
# ukazuju na to da je mnogo piksela te vrijednosti prisutno u slici.

img_color = cv2.imread("img/primjer_1.png")
color_channels = ('b', 'g', 'r')
plt.figure(figsize=(10,5))
for i, col in enumerate(color_channels):
    hist = cv2.calcHist([img_color], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

# plt.title("Histogram za svaki kanal boje")
# plt.xlabel("Intenzitet piksela")
# plt.ylabel("Broj piksela")
# plt.show()
# Modifikacija: Prikaz histograma za svaki kanal boje u istom grafu s različitim bojama za bolju vizualizaciju.






"""
2.
Zadatak
Učitaj sliku primjer_2.jpg kao sliku u sivim tonovima. Primijeni jednostavno ujednačavanje histograma. Prikaži dobiveni rezultat
"""

img_gray = cv2.imread("img/primjer_2.jpg", cv2.IMREAD_GRAYSCALE)
equalized_img = cv2.equalizeHist(img_gray)
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title("Originalna slika")
plt.subplot(1, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title("Ujednačena slika")
plt.show()


"""
3.
Zadatak
Učitaj sliku primjer_3.png kao sliku u boji.
a)
Pretvori sliku u boji u sliku sa sivim tonovima.
b)
Primijeni jednostavno ujednačavanje histograma. Prikaži dobiveni rezultat.
c)
Primijeni adaptivno ujednačavanje histograma. Prikaži dobiveni rezultat.
d)
Usporedite dobiveni rezultat i histograme pod b) i c)

"""

#b, c i d
img_3 = cv2.imread("img/primjer_3.png", cv2.IMREAD_GRAYSCALE)
equalized_img_3 = cv2.equalizeHist(img_3)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
adaptive_equalized_img_3 = clahe.apply(img_3)
plt.figure(figsize=(15,5))
plt.subplot(1, 3, 1)
plt.imshow(img_3, cmap='gray')
plt.title("Originalna slika")
plt.subplot(1, 3, 2)
plt.imshow(equalized_img_3, cmap='gray')
plt.title("Ujednačena slika")
plt.subplot(1, 3, 3)
plt.imshow(adaptive_equalized_img_3, cmap='gray')
plt.title("Adaptivno ujednačena slika")
plt.show()
































