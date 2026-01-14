import cv2
import numpy as np

"""
1. Zadatak
Pomoću OpenCV-a učitajte sliku koja je snimljena s kamere automobila pod nazivom “kamera3.jpg”. Sliku učitajte u 
nijansama sive boje. Ispišite na ekran dimenzije slike
"""

img_1 = cv2.imread("img/kamera3.jpg", cv2.IMREAD_GRAYSCALE)
print("Dimenzije slike kamera3.jpg su:", img_1.shape)


"""
2. Zadatak
Pomoću OpenCV-a učitajte sliku koja je snimljena s kamere automobila pod nazivom “kamera3.jpg”. Ispišite na ekran 
dimenzije slike. Promijenite veličinu slike na 1000x650.
"""

img_2 = cv2.imread("img/kamera3.jpg")
print("Dimenzije slike kamera3.jpg su:", img_2.shape)
resized_img_2 = cv2.resize(img_2, (1000, 650))
print("Dimenzije promijenjene slike su:", resized_img_2.shape)

"""
3. Zadatak
Pomoću OpenCV-a učitajte sliku koja je snimljena s kamere automobila pod nazivom “kamera3.jpg”. Zaokrenite sliku po x i y osi, 
prikažite ju, te spremite pod nazivom “zaokrenuta_slika.jpg”.
"""

img_3 = cv2.imread("img/kamera3.jpg")
flipped_img_3 = cv2.flip(img_3, -1)  # -1 = both axes
# cv2.imshow("Zaokrenuta slika", flipped_img_3)
# cv2.imwrite("img/zaokrenuta_slika.jpg", flipped_img_3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""
4. Zadatak
Pomoću OpenCV-a učitajte sliku koja je snimljena s kamere automobila pod nazivom “kamera3.jpg”. Promijenite vrijednost 
piksela koji čine dio registracijske oznake automobila koji se nalazi ispred nas u žutu boju.

"""
img_4 = cv2.imread("img/kamera3.jpg")
img_4_hsv = cv2.cvtColor(img_4, cv2.COLOR_BGR2HSV)
cv2.imshow("Originalna slika", img_4)
# Pretpostavimo da je registracijska oznaka unutar određenog raspona boja u HSV prostoru

lower_bound = np.array([0, 0, 0])
upper_bound = np.array([0, 255, 255])

mask = cv2.inRange(img_4_hsv, lower_bound, upper_bound)
result = cv2.bitwise_and(img_4, img_4, mask=mask)
# img_4[mask > 0] = [0, 255, 255]  # Postavi na žutu boju u BGR
cv2.imshow("4. Modificirana slika", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


















