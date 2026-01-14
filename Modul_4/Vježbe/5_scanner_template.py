import cv2
import numpy as np


# ---------------- 1) UČITAVANJE I PREPROCESSING ----------------

img = cv2.imread('img/dokument.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise SystemExit("Ne mogu učitati sliku 'upute.jpg'.")

orig = img.copy()
#cv2.imshow("1 - original", orig)

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("2 - gray", gray)

# blur (smanjenje šuma)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow("3 - blur", blur)

# Otsu threshold – papir bijel, stol taman
_, thresh = cv2.threshold(
    blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
#cv2.imshow("4 - thresh (Otsu)", thresh)

# malo morfološko zatvaranje da rub papira bude kompaktan
kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
#closed = cv2.morphologyEx(thresh, kernel=cv2.MORPH_CLOSE, kernel=kernel_close, iterations=2)
# # ako ti gornja linija baci error zbog keyword argumenata, koristi:
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_close, iterations=2)
cv2.imshow("5 - morph CLOSE", closed)

# ---------------- 2) KONTURE – ZADATAK ZA VAS ----------------
# OVDJE TREBATE POPUNITI KOD TAKO DA DEFINIRATE SLJEDEĆE VARIJABLE:
#   - contours  : lista svih pronađenih kontura
#   - paper_cnt : najveća kontura (papir)
#   - peri      : opseg konture papira
#   - approx    : aproksimirana kontura (poligon, npr. 4 točke za papir)
#   - debug_paper : kopija originalne slike s nacrtanom aproksimiranom konturom

# === TODO 1: pronađi sve vanjske konture na slici 'closed' ===
#   koristi cv2.findContours(...)
#
# contours, hierarchy = ...
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# === TODO 2: ako nema kontura, prekini program s porukom ===
#
if len(contours) == 0:
    raise SystemExit("Nije pronađena nijedna kontura na slici.")

# === TODO 3: sortiraj konture po površini i uzmi najveću kao 'paper_cnt' ===
#
# paper_cnt = ...
contours = sorted(contours, key=cv2.contourArea, reverse=True)
paper_cnt = contours[0]


# === TODO 4: izračunaj opseg i aproksimiraj konturu papira poligonom ===
#
# peri = ...
# approx = ...
peri = cv2.arcLength(paper_cnt, True)
approx = cv2.approxPolyDP(paper_cnt, 0.02 * peri, True)


# === TODO 5: nacrtaj aproksimiranu konturu na kopiji originala ===
debug_paper = orig.copy()


# (opcionalno) ispis broja vrhova aproksimirane konture
try:
    print("Broj vrhova aproksimirane konture:", len(approx))
except NameError:
    print("TODO dio s konturama NIJE dovršen - 'approx' nije definiran.")

cv2.imshow("6 - pronađen papir (kontura)", debug_paper)

# Ako studenti nisu dobro popunili dio s konturama, zaustavi dalje:
if 'approx' not in locals() or 'paper_cnt' not in locals():
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    raise SystemExit("Najprije dovršite dio s konturama (2. blok)!")

# ---------------- 3) PERSPEKTIVNA TRANSFORMACIJA ----------------

def order_points(pts):
    # pts shape: (4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    rect[0] = pts[np.argmin(s)]      # top-left
    rect[2] = pts[np.argmax(s)]      # bottom-right
    rect[1] = pts[np.argmin(diff)]   # top-right
    rect[3] = pts[np.argmax(diff)]   # bottom-left
    return rect

# ako aproksimacija nema točno 4 točke, koristi boundingRect kao fallback
if len(approx) == 4:
    pts = approx.reshape(4, 2).astype("float32")
else:
    print("Upozorenje: approx nema 4 točke – koristim boundingRect kao fallback.")
    x, y, w, h = cv2.boundingRect(paper_cnt)
    pts = np.array([
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h]
    ], dtype="float32")

rect = order_points(pts)
(tl, tr, br, bl) = rect

# dimenzije "ispravljenog" papira
widthA = np.linalg.norm(br - bl)
widthB = np.linalg.norm(tr - tl)
maxWidth = int(max(widthA, widthB))

heightA = np.linalg.norm(tr - br)
heightB = np.linalg.norm(tl - bl)
maxHeight = int(max(heightA, heightB))

dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]
], dtype="float32")

M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
cv2.imshow("7 - ispravljeni papir (color)", warped)

# ---------------- 4) "SCANNER" EFEKT – CRNO/BIJELO (OTSU + CLOSING) ----------------

warp_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warp_blur = cv2.GaussianBlur(warp_gray, (5, 5), 0)

_, scan = cv2.threshold(
    warp_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
cv2.imshow("8 - scan (Otsu)", scan)

# invert -> slova bijela, pozadina crna
scan_inv = cv2.bitwise_not(scan)

# vertikalni CLOSING (1x3) – popunjava sitne rupe u potezima
kernel_close2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
scan_inv_closed = cv2.morphologyEx(scan_inv, cv2.MORPH_CLOSE, kernel_close2, iterations=1)

# vrati natrag: slova crna, pozadina bijela
scan_clean = cv2.bitwise_not(scan_inv_closed)
cv2.imshow("9 - scan (Otsu + vert closing)", scan_clean)

# ---------------- 5) SPOJENI PRIKAZ KORAKA ----------------

thresh_bgr = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
scan_bgr = cv2.cvtColor(scan_clean, cv2.COLOR_GRAY2BGR)

scale = 0.5  # smanji da stane na ekran

def resize(img):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

row1 = cv2.hconcat([resize(orig), resize(thresh_bgr), resize(debug_paper)])
row2 = cv2.hconcat([resize(warped), resize(scan_bgr)])

# poravnaj širine redova ako treba
target_width = max(row1.shape[1], row2.shape[1])

def pad_to_width(img, width):
    if img.shape[1] == width:
        return img
    pad = width - img.shape[1]
    return cv2.copyMakeBorder(img, 0, 0, 0, pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

row1 = pad_to_width(row1, target_width)
row2 = pad_to_width(row2, target_width)

concat = cv2.vconcat([row1, row2])
cv2.imshow("Svi koraci (original | Otsu | kontura | warp | scan clean)", concat)

# ---------------- 6) SPREMANJE REZULTATA ----------------

cv2.imwrite("upute_warp_color.png", warped)
cv2.imwrite("upute_scan_bw.png", scan_clean)
cv2.imwrite("upute_svi_koraci.png", concat)

cv2.waitKey(0)
cv2.destroyAllWindows()
