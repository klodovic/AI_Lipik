import cv2
import numpy as np
import scanner_template as scanner

# Zadatak 1:
"""
Napisati program koji:
•automatski pronađe sve kekse na slici,
•prepozna koji je keks oštećen,
•vizualno označi rezultat tako da:
•svi cijeli keksi budu prekriveni zelenim poluprozirnim overlay-em,
•oštećeni keks bude prekriven crvenim poluprozirnim overlay-em,
•na kraju prikaže konačnu sliku rezultata (original s obojenim keksima),a po mogućnosti i sažeti prikaz važnih međukoraka 
obrade (npr. original, binarna slika, konture, rezultat).

•Upute (smjernice, ne nužno doslovno ovim redoslijedom,nitisesvemoraprimijeniti)
•pretvoriti sliku u grayscale,
•ukloniti šum (npr. Gaussian blur),
•napraviti binarnu slike (npr. Otsu threshold),
•primijeniti morfološke operacije (npr. closing) kako bi keksi bili kompaktni objekti,
•pronaći konture keksa (findContours) i filtrirati samo veće objekte (kekse) prema njihovoj površini,
•za svaki keks izračunati površinu konture i na temelju toga odrediti koji keks se značajno razlikuje od ostalih (npr. najmanja površina ili najveće odstupanje od medijana površine),
•nacrtati obojani overlay za svaki keks:
•cijeli → zeleno,
•oštećeni → crveno,
•kombinirati overlay s originalnom slikom (npr. addWeighted) tako da se original još uvijek vidi ispod boje.

"""

img = cv2.imread('img/keksi.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = [c for c in contours if cv2.contourArea(c) > 800]   

circularities = []
for c in contours:
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    circularities.append(circularity)

damaged_cookie_index = np.argmin(circularities)

overlay = img.copy()
for i, contour in enumerate(contours):
    if i == damaged_cookie_index:
        color = (0, 0, 255)    # oštećeni
    else:
        color = (0, 255, 0)    # cijeli
    cv2.drawContours(overlay, [contour], -1, color, -1)

final_image = cv2.addWeighted(img, 0.7, overlay, 0.3, 0)
cv2.imshow("Rezultat - Kekse detektirani", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()





