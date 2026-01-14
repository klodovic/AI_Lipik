import cv2
import numpy as np

# ----------------------------------------
# POSTAVKE
# ----------------------------------------
VIDEO_PATH = "video/primjer_8.mp4"   # promijeni po potrebi

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise SystemExit("Ne mogu otvoriti video datoteku.")

# učitaj prvi frame
ret, frame1 = cap.read()
if not ret:
    raise SystemExit("Ne mogu pročitati prvi frame.")

prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

win_name = "Gusti optički tok - strelice (Farneback)"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win_name, 960, 540)

# korak mreže (što veći, to manje strelica)
STEP = 10

# faktor skaliranja duljine strelica (da se bolje vidi)
SCALE = 5

# ----------------------------------------
# GLAVNA PETLJA
# ----------------------------------------
while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # izračunaj gusti optički tok (Farneback)
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray, gray, None,
        pyr_scale=0.5,
        levels=3,
        winsize=15,
        iterations=3,
        poly_n=5,
        poly_sigma=1.2,
        flags=0
    )

    # kopija framea za crtanje
    vis = frame2.copy()

    h, w = gray.shape

    # prolazimo po mreži točaka (svakih STEP piksela)
    for y in range(0, h, STEP):
        for x in range(0, w, STEP):
            fx, fy = flow[y, x]   # vektor gibanja u toj točki

            # početna točka strelice
            x1 = int(x)
            y1 = int(y)

            # krajnja točka (skalirani vektor)
            x2 = int(x + fx * SCALE)
            y2 = int(y + fy * SCALE)

            # nacrtaj strelicu
            cv2.arrowedLine(
                vis,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                1,
                tipLength=0.3
            )

    cv2.imshow(win_name, vis)

    key = cv2.waitKey(30) & 0xFF
    if key == 113:  # 'q' – izlaz
        break

    # trenutni gray postaje "prethodni" za sljedeći korak
    prev_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()
