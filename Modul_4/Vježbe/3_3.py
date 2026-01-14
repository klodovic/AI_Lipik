import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
1.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji. Rotirajte sliku za 10° u smjeru kazaljke na sati. Veličina izlazne 
slike treba biti jednaka veličini ulazne slike. Koristite funkciju cv2.warpAffine().
"""

img = cv2.imread("img/primjer_3_1.png")
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -10, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))
# cv2.imshow("Originalna slika", img)
# cv2.imshow("Rotirana slika", rotated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""
2.
Zadatak
Učitaj sliku primjer_1.png kao sliku u boji. Rotiraj sliku za 90° u smjeru kazaljke na satu oko njezina središta i 
skaliraj je faktorom 0,5. Veličina izlazne slike treba biti jednaka veličini ulazne slike. 
Koristi funkciju cv2.getRotationMatrix2D.
"""

img_1 = cv2.imread("img/primjer_3_1.png")
(h1, w1) = img_1.shape[:2]
center1 = (w1 // 2, h1 // 2)
M1 = cv2.getRotationMatrix2D(center1, -90, 0.5)
rotated_scaled_img = cv2.warpAffine(img_1, M1, (w1, h1))
# cv2.imshow("Originalna slika", img_1)
# cv2.imshow("Rotirana i skalirana slika", rotated_scaled_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""
3.
Zadatak
Učitaj sliku primjer_2.jpg kao sliku u boji. Prikaži sliku pomoću matplotlib biblioteke. Pronađi transformacijsku 
matricu kojom ćete dobiti pogled odozgor. Transformiraj pomoću matrice ulaznu sliku. Rezultat treba biti kao što 
je prikazano na slici.
"""

img_2 = cv2.imread("img/primjer_3_2.jpg")
# Definiranje točaka za perspektivnu transformaciju
# points1 = np.float32([
#     [35, 394],    # gornji lijevi
#     [290, 738],   # donji lijevi
#     [464, 160],   # gornji desni
#     [729, 377]    # donji desni
# ])
points1 = np.float32([[290,738],[729,377],[35, 394],[464, 160]])
points2 = np.float32([[0,0],[0,600],[430,0],[430,600]])

matrix = cv2.getPerspectiveTransform(points1, points2)
result = cv2.warpPerspective(img_2, matrix, (430, 600))
cv2.imshow("Orig slika", img_2)
cv2.imshow("Transformirana slika", result)
cv2.waitKey(0)
cv2.destroyAllWindows()



















