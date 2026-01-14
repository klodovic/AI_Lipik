import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
1.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji i pretvori je u sliku sa sivim tonovima (engl. grayscale).
a)
Primijeni eroziju na sliku u sivim tonovima:
•
pravokutni strukturni element 3x3, jedna iteracija
•
pravokutni strukturni element 3x3, dvije iteracije
Usporedi slike jednu pored druge i komentiraj rezultate s obzirom na obradu šuma i rupa (praznina).
b)
Promijeni veličinu strukturnog elementa i ponovno primijeni eroziju.Što se događa kada je strukturni element prevelik ili premalen?
c)
Promijeni omjer stranica strukturnog elementa (npr. 3x5). Što primjećujete?
"""

img = cv2.imread("img/primjer_2_1.png", cv2.IMREAD_GRAYSCALE)

# a) Erozija s pravokutnim strukturnim elementom 3x3, jedna iteracija
kernel_3x3 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # originalno 3x3
eroded_1_iter = cv2.erode(img, kernel_3x3, iterations=1)
eroded_2_iter = cv2.erode(img, kernel_3x3, iterations=2)
# plt.figure(figsize=(15,5))
# plt.subplot(1, 3, 1)
# plt.imshow(img, cmap='gray')
# plt.title("Originalna slika")
# plt.subplot(1, 3, 2)
# plt.imshow(eroded_1_iter, cmap='gray')
# plt.title("Erozija 1 iteracija")
# plt.subplot(1, 3, 3)
# plt.imshow(eroded_2_iter, cmap='gray')
# plt.title("Erozija 2 iteracije")
# plt.show()

#zaključak:
# erozija s 3x3 treba dvije iteracije da bi se vidio značajan efekt uklanjanja šuma i smanjenja rupam dok 
# 5x5 uklanja više šuma i rupa već nakon jedne iteracije.



# c) Promjena omjera stranica strukturnog elementa na 3x5
kernel_3x5 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
eroded_3x5 = cv2.erode(img, kernel_3x5, iterations=1)
# plt.figure(figsize=(10,5))
# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title("Originalna slika")
# plt.subplot(1, 2, 2)
# plt.imshow(eroded_3x5, cmap='gray')
# plt.title("Erozija s 3x5 kernelom")
# plt.show()
#zaključak:
# Erozija s 3x5 kernelom uzrokuje da se vertikalni elementi smanje više nego horizontalni, što može biti korisno
# za uklanjanje vertikalnih šumova ili isticanje horizontalnih značajki na slici.

"""
2.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji i pretvori je u sliku sa sivim tonovima (engl. grayscale).
a)
Primijeni dilataciju na sliku u sivim tonovima:
•
pravokutni strukturni element 3x3, jedna iteracija
•
pravokutni strukturni element 3x3, dvije iteracije
Usporedi slike jednu pored druge i komentiraj rezultate s obzirom na obradu šuma i rupa (praznina).
b)
Promijeni veličinu strukturnog elementa i ponovno primijeni eroziju.Što se događa kada je strukturni element prevelik ili premalen?
c)
Promijeni omjer stranica strukturnog elementa (npr. 3x5). Što primjećujete?
"""



img_2 = cv2.imread("img/primjer_2_1.png", cv2.IMREAD_GRAYSCALE)
# a) Dilatacija s pravokutnim strukturnim elementom 3x3, jedna iteracija
kernel_3x3 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilated_1_iter = cv2.dilate(img_2, kernel_3x3, iterations=1)
dilated_2_iter = cv2.dilate(img_2, kernel_3x3, iterations=2)
# plt.figure(figsize=(15,5))
# plt.subplot(1, 3, 1)
# plt.imshow(img_2, cmap='gray')
# plt.title("Originalna slika")
# plt.subplot(1, 3, 2)
# plt.imshow(dilated_1_iter, cmap='gray')
# plt.title("Dilatacija 1 iteracija")
# plt.subplot(1, 3, 3)
# plt.imshow(dilated_2_iter, cmap='gray')
# plt.title("Dilatacija 2 iteracije")
# plt.show()

#zaključak: diletacija s 3x3 kernelom širi svijetle dijelove slike, što može pomoći u zatvaranju malih rupa i 
# povezivanju prekida u svijetlim područjima. Veći kernel (5x5) dodatno pojačava ovaj efekt, ali može također 
# uzrokovati gubitak detalja.

# c) Promjena omjera stranica strukturnog elementa na 3x5
kernel_3x5 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
dilated_3x5 = cv2.dilate(img_2, kernel_3x5, iterations=1)
# plt.figure(figsize=(10,5))
# plt.subplot(1, 2, 1)
# plt.imshow(img_2, cmap='gray')
# plt.title("Originalna slika")
# plt.subplot(1, 2, 2)
# plt.imshow(dilated_3x5, cmap='gray')
# plt.title("Dilatacija s 3x5 kernelom")
# plt.show()

#zaključak: Dilatacija s 3x5 kernelom uzrokuje da se horizontalni elementi prošire više nego vertikalni, što može biti korisno
# za povezivanje horizontalnih značajki ili uklanjanje horizontalnih prekida na slici.


"""
3.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji i pretvori je u sliku sa sivim tonovima (engl. grayscale).
a)
Primijeni otvaranje i zatvaranje na sliku u sivim tonovima:
•
pravokutni strukturni element 3x3, jedna iteracija
•
pravokutni strukturni element 3x3, dvije iteracije
Morfološke transformacije
Usporedi slike jednu pored druge i komentiraj rezultate s obzirom na obradu šuma i rupa (praznina).
b)
Promijeni veličinu strukturnog elementa i ponovno primijeni eroziju.Što se događa kada je strukturni element prevelik ili premalen?
c)
Promijeni omjer stranica strukturnog elementa (npr. 3x5). Što primjećujete?
"""

img_3 = cv2.imread("img/primjer_2_1.png", cv2.IMREAD_GRAYSCALE)
# a) Otvaranje i zatvaranje s pravokutnim strukturnim elementom 3x3, jedna iteracija
kernel_3x3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened_1_iter = cv2.morphologyEx(img_3, cv2.MORPH_OPEN, kernel_3x3, iterations=1)
closed_1_iter = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel_3x3, iterations=1)
opened_2_iter = cv2.morphologyEx(img_3, cv2.MORPH_OPEN, kernel_3x3, iterations=2)
closed_2_iter = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel_3x3, iterations=2)
# plt.figure(figsize=(15,10))
# plt.subplot(2, 3, 1)
# plt.imshow(img_3, cmap='gray')
# plt.title("Originalna slika")
# plt.subplot(2, 3, 2)
# plt.imshow(opened_1_iter, cmap='gray')
# plt.title("Otvaranje 1 iteracija")
# plt.subplot(2, 3, 3)
# plt.imshow(closed_1_iter, cmap='gray')
# plt.title("Zatvaranje 1 iteracija")
# plt.subplot(2, 3, 5)
# plt.imshow(opened_2_iter, cmap='gray')
# plt.title("Otvaranje 2 iteracije")
# plt.subplot(2, 3, 6)
# plt.imshow(closed_2_iter, cmap='gray')
# plt.title("Zatvaranje 2 iteracije")
# plt.show()

#zaključak: Otvaranje pomaže u uklanjanju malih svijetlih šumova dok zatvaranje pomaže u zatvaranju malih tamnih rupa. 
# Veći kernel (5x5) dodatno pojačava ove efekte, ali može također uzrokovati gubitak detalja.

# c) Promjena omjera stranica strukturnog elementa na 3x5
kernel_3x5 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
opened_3x5 = cv2.morphologyEx(img_3, cv2.MORPH_OPEN, kernel_3x5, iterations=1)
closed_3x5 = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel_3x5, iterations=1)
# plt.figure(figsize=(10,5))
# plt.subplot(1, 2, 1)
# plt.imshow(opened_3x5, cmap='gray')
# plt.title("Otvaranje s 3x5 kernelom")
# plt.subplot(1, 2, 2)
# plt.imshow(closed_3x5, cmap='gray')
# plt.title("Zatvaranje s 3x5 kernelom")
# plt.show()

#zaključak: Otvaranje i zatvaranje s 3x5 kernelom uzrokuje da se horizontalne značajke obrađuju više nego vertikalne,
# što može biti korisno za specifične obrade slika ovisno o orijentaciji značajki na slici.

"""
4.
Zadatak (samostalni rad)
Učitaj sliku primjer_2.png koja prikazuje oštećeni barkod. Iskoristi morfološke transformacije za njegovo obnavljanje 
(rekonstrukciju) kao što je prikazano na slici.
"""

img_4 = cv2.imread("img/primjer_2_2.png", cv2.IMREAD_GRAYSCALE)
# Primjena morfoloških operacija za rekonstrukciju barkoda
kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 13))
kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
# Prvo primijenimo zatvaranje kako bismo popunili praznine
closed = cv2.morphologyEx(img_4, cv2.MORPH_CLOSE, kernel_close, iterations=2)
# Zatim primijenimo otvaranje kako bismo uklonili šum
opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel_open, iterations=2)
# Prikaz rezultata

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(img_4, cmap='gray')
plt.title("Originalna oštećena slika")
plt.subplot(1, 2, 2)
plt.imshow(opened, cmap='gray')
plt.title("Rekonstruirani barkod")
plt.show()


#zaključak: Korištenjem kombinacije zatvaranja i otvaranja s odgovarajućim kernelom, uspjeli smo značajno poboljšati
# kvalitetu barkoda uklanjanjem šuma i popunjavanjem praznina, čineći ga čitljivijim.