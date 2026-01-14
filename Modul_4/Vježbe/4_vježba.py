import cv2
import numpy as np  


# Zadatak 1:

"""
Korištenjem standardne Houghove transformacije detektirajte i nacrtajte linije na slici 
“autocesta.jpeg”. Među detektiranim linijama moraju biti prepoznate i linije voznih traka.
Podešavanjem sljedećih parametara pokušajte što preciznije izdvojiti upravo linije voznih 
traka, te pritom isprobajte različite vrijednosti tih parametara kako biste uočili njihov 
utjecaj na rezultat:
● prag 1 za Canny detekciju rubova
● prag 2 za Canny detekciju rubova
● ρ rezolucija
● θ rezolucija
● prag Houghovog akumulatora

"""

image_bgr = cv2.imread('img/autocesta.jpeg', cv2.IMREAD_COLOR)
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image_gray, 50, 150) # pragovi za Canny detekciju rubova
lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 200, threshold=370) # prag Houghovog akumulatora

if lines is not None: 
    for line in lines: 
        rho, theta = line[0] 

        a = np.cos(theta) 
        b = np.sin(theta) 
        x0 = a * rho 
        y0 = b * rho 

        x1 = int(x0 + 1000 * (-b)) 
        y1 = int(y0 + 1000 * (a)) 
        x2 = int(x0 - 1000 * (-b)) 
        y2 = int(y0 - 1000 * (a)) 

        cv2.line(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow('Zadatak 1: Detected Lines', image_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# Zadatak 2:

"""
Ponovite prethodni zadatak, ali ovoga puta koristeći probabilističku Houghovu transformaciju za 
detekciju linijskih segmenata na slici “autocesta.jpeg”. Među detektiranim segmentima ponovno 
moraju biti prepoznate linije voznih traka.
Uz postojeće parametre (prag 1 i prag 2 za Canny, rezolucije ρ i θ, te prag Houghovog akumulatora), 
dodatno eksperimentirajte i s dva nova parametra probabilističke metode:
● minLineLength
● maxLineGap
Isprobajte različite vrijednosti svih parametara kako biste uočili njihov utjecaj na kvalitetu 
detekcije linija voznih traka.
Koje su glavne razlike standardne i probabilističke Houghove transformacije?

"""

image_bgr = cv2.imread('img/autocesta.jpeg', cv2.IMREAD_COLOR)
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image_gray, 200, 400) # pragovi za Canny detekciju rubova
lines = cv2.HoughLinesP(
    edges, 
    rho=1, 
    theta=np.pi / 200, 
    threshold=200, 
    minLineLength=300, 
    maxLineGap=20
    )

if lines is not None: 
    for line in lines: 
        x1, y1, x2, y2 = line[0] 
        cv2.line(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow('Zadatak 2: Detected Line Segments', image_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Zadatak 3:
"""
U prethodnom zadatku vidljivo je da je teško pouzdano izdvojiti samo linije voznih traka, jer se 
detektiraju i mnoge druge linije na slici. Kako biste smanjili broj neželjenih linija, primijenite 
maskiranje slike i pokušajte izdvojiti samo područje u kojem se očekuju linije voznih traka.
Preporučuje se kao masku koristiti gornju polovicu elipse postavljene u donjem dijelu slike, 
tako da maskirate samo relevantni dio kolnika.
"""

image_gray = cv2.imread('img/autocesta.jpeg', cv2.IMREAD_GRAYSCALE)
mask = np.ones_like(image_gray)
height, width = mask.shape

x1 = width // 2
y1 = height // 4
x2 = 0
y2 = height
x3 = width
y3 = height

rectangle_points = np.array([[(x1, y1)], [(x2, y2)], [(x3, y3)]], dtype=np.int32)  
mask = cv2.fillPoly(mask, [rectangle_points], 255) # Ispunjavanje maske bijelom bojom unutar definiranog poligona
masked_image = cv2.bitwise_and(image_gray, mask)

# cv2.imshow("Maska prije elipse", mask)
# cv2.imshow("Originalna slika", image_gray)
# cv2.imshow("Maskirana slika", masked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Zadatak 4:

"""
Metodom maskiranja slike i korištenjem Houghove transformacije, pokušajte detektirati prometni 
znak na slici “kamera4.png”. Kako bi detekcija bila preciznija, maskirajte desni dio slike, gdje 
se prometni znak uobičajeno nalazi.
"""

image_4 = cv2.imread('img/kamera4.png')
image_gray4 = cv2.cvtColor(image_4, cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(image_gray4)

height, width = mask.shape

x1 = width // 2 
y1 = 0
x2 = width -1
y2 = 0
x3 = width -1
y3 = height -1
x4 = width // 2
y4 = height -1

# Definiranje točaka poligona (pravokutnika)
rectangle_points = np.array([[(x1, y1)], [(x2, y2)], [(x3, y3)], [(x4, y4)]], dtype=np.int32)  
mask = cv2.fillPoly(mask, [rectangle_points], 255) # Ispunjavanje maske bijelom bojom unutar definiranog poligona
masked_image = cv2.bitwise_and(image_gray4, mask) # Primjena maske na originalnu sliku

blured_image = cv2.medianBlur(masked_image, 5)

circles = cv2.HoughCircles(
    blured_image,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=120,
    param2=35,
    minRadius=20,
    maxRadius=120
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image_gray4, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(image_gray4, (i[0], i[1]), 2, (0, 0, 255), 3)
else:
    print("No circles detected.")

cv2.imshow('Zadatak 4: Detected Circles', image_4)
cv2.waitKey(0)
cv2.destroyAllWindows()







