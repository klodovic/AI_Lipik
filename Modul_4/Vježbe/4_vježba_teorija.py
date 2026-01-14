import cv2
import numpy as np  


# Primjer 1: (cv2.HoughLines())
# Standardna Houghova transformacija
# Učitaj sliku
image_bgr = cv2.imread('img/lanes.jpg', cv2.IMREAD_COLOR)

# Houghova transformacija za detekciju linija
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(image_gray, 100, 200) # 100 i 200 su pragovi za Canny detekciju rubova (default)
lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=180)

# Iscrtavanje detektovanih linija na originalnu sliku
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

# Prikaz rezultata
# cv2.imshow('Primjer 1: Detected Lanes', image_bgr)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()


#___________________________________________________________________________________________


#Primjer 2: (cv2.HoughLinesP())
# Probabilistička Houghova transformacija (random metoda - brže izvođenje)

# Učitaj sliku
image_bgr = cv2.imread('img/lanes.jpg', cv2.IMREAD_COLOR)

# Houghova transformacija za detekciju linija
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(image_gray, 100, 200) # 100 i 200 su pragovi za Canny detekciju rubova (default)

# HoughLinesP ima u sebi blur i ne treba dodatno raditi
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=80, minLineLength=100, maxLineGap=20)

# Iscrtavanje detektovanih linija na originalnu sliku
if lines is not None: 
    for line in lines: 
        x1, y1, x2, y2 = line[0] 
        cv2.line(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 2)
else:
    print("No lines detected.")

# Prikaz rezultata
# cv2.imshow('Primjer 2: Detected Lanes - Probabilistic Hough', image_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#___________________________________________________________________________________________


# Primjer 3: Detekcija kružnica - HoughCircles()

# Učitaj sliku
image_bgr = cv2.imread('img/coins.png', cv2.IMREAD_COLOR)

# Houghova transformacija za detekciju kružnica
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
image_gray = cv2.medianBlur(image_gray, 5)  # Smanji šum pomoću medijanskog filtera, kerenel veličine 5

# HoughCircles ne radi blur, pa je potrebno prethodno obraditi sliku medijanBlur-om
circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=100, param2=70, minRadius=15, maxRadius=100)

# Iscrtavanje detektovanih kružnica na originalnu sliku
if circles is not None:
    circles = np.uint16(np.around(circles)) # circle parametri su float, pa ih pretvaramo u uint16
    for i in circles[0, :]:
        # Iscrtavanje vanjskog kruga
        cv2.circle(image_bgr, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Iscrtavanje centra kružnice
        cv2.circle(image_bgr, (i[0], i[1]), 2, (0, 0, 255), 3)
else:
    print("No circles detected.")

# Prikaz rezultata
# cv2.imshow('Primjer 3: Detected Circles', image_bgr)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

#___________________________________________________________________________________________


# Primjer 4: Maskiranje slike pomoću poligona - rectangle

# Učitaj sliku
image_gray = cv2.imread('img/kamera4.png', cv2.IMREAD_GRAYSCALE)
mask = np.zeros_like(image_gray)

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
masked_image = cv2.bitwise_and(image_gray, mask) # Primjena maske na originalnu sliku

# cv2.imshow('Original Image', image_gray)
# cv2.imshow('Masked Image', masked_image)
# cv2.imshow('Mask', mask)    
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#___________________________________________________________________________________________


# Primjer 5: Maskiranje slike pomoću poligona - elipsa

HEIGHT = 500
WIDTH = 700

maks = np.zeros((HEIGHT, WIDTH))

cv2.ellipse(maks, 
            center=(WIDTH // 2, HEIGHT // 2), 
            axes=(WIDTH // 2, HEIGHT // 2), 
            angle=0, 
            startAngle=180, 
            endAngle=360, 
            color=255, 
            thickness=-1 # ispunjeno = -1
            )

# cv2.imshow('Elipsa', maks)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#___________________________________________________________________________________________


# Primjer 6: Video petlja
#capture = cv2.VideoCapture("img/autocesta_video.mp4")
capture = cv2.VideoCapture(0)  # Koristi kameru računala

if not capture.isOpened():
    print("Error opening video file")
    exit(1)


while True:
    ret, frame = capture.read()
    if frame is None:
        break

    cv2.imshow('Video Frame', frame)
    if cv2.waitKey(100) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()







