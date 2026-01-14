import cv2
import numpy as np

# ----------------------------------------
# Postavke
# ----------------------------------------
VIDEO_PATH = "video/primjer_4.avi"

cap = cv2.VideoCapture(VIDEO_PATH)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ----------------------------------------
# 1) UČITAJ PRVI FRAME I ODABERI ROI
# ----------------------------------------

ret, frame = cap.read()
if not ret:
    raise SystemExit("Ne mogu pročitati prvi frame iz videa.")

cv2.imshow("Select object to track", frame)

# TODO: koristiti cv2.selectROI za odabir početnog prozora, izlaz u varijablu track_window
track_window = cv2.selectROI(frame) # zamijeniti s pozivom cv2.selectROI(...)


cv2.destroyWindow("Select object to track")

# TODO: raspakirati track_window u x, y, w, h te izračunati vrhove track_window
x, y, w, h = track_window

# TODO: izdvoji odabrani dio slike i spremi ga u varijablu roi koristeći NumPy slicing i dobivene vrijednosti x1, y1, x2, y2
# Izračun vrhova
x1, y1 = x, y
x2, y2 = x + w, y + h

# Izdvajanje ROI-a
roi = frame[y1:y2, x1:x2]

# ----------------------------------------
# 2) PRIPREMI HSV HISTOGRAM ROI-A
# ----------------------------------------

# TODO: koristiti cv2.cvtColor za pretvorbu ROI u HSV, izlaz u varijablu hsv_roi
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) # pretvoriti roi u HSV

# TODO: koristiti cv2.calcHist za računanje histograma H kanala, izlaz u varijablu roi_hist
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180]) # izračunati histogram H kanala

# TODO: koristiti cv2.normalize za normalizaciju histograma u raspon 0–255, izlaz isto roi_hist
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# kriterij zaustavljanja: max 10 iteracija ili pomak barem 1 piksel
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)


# ----------------------------------------
# 3) GLAVNA PETLJA PO FRAMEOVIMA
# ----------------------------------------
while True:

    ret, frame = cap.read()
    if not ret:
        break

    # TODO: koristiti cv2.cvtColor za pretvorbu framea u HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # pretvoriti frame u HSV

    # TODO: koristiti cv2.calcBackProject za računanje back-projekcije,
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)  # izračunati back-projekciju

    # ----------------------------------------
    # 4) PRIMJENI TRACKING (MEANSHIFT ILI CAMSHIFT)
    # ----------------------------------------
    # TODO: primijeniti praćenje pozivom cv2.meanShift(...) ILI cv2.CamShift(...)
    #ret, track_window = cv2.meanShift(dst, track_window, term_crit)  # pozvati odabranu funkciju za praćenje
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)  # pozvati odabranu funkciju za praćenje

    # Ako koristite CamShift, iz ret možete dobiti 4 vrha pravokutnika preko cv2.boxPoints(ret)
    # Ako koristite MeanShift, koristite track_window = (x, y, w, h)

    # TODO: nacrtati rezultat praćenja na frame:
    #       - za MeanShift: cv2.rectangle(...)
    #       - za CamShift:  cv2.boxPoints(...) + cv2.polylines(...)
    x, y, w, h = track_window
    cv2.rectangle(frame,(int(x), int(y)),(int(x + w), int(y + h)),(0, 255, 0),2)


    # ----------------------------------------
    # 5) PRIKAZ
    # ----------------------------------------
    cv2.imshow("Tracking", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 113:  # 'q' za izlaz
        break

    # 't' za ponovni odabir cilja u trenutnom frameu

    # ----------------------------------------
    # ZADATAK 2
    # ----------------------------------------
    if key == ord('t'):  # 't'
        new_roi = cv2.selectROI("Select new target", frame)
        cv2.destroyWindow("Select new target")

        x, y, w, h = new_roi
        track_window = (x, y, w, h)

        roi = frame[y:y+h, x:x+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
        roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# ----------------------------------------
# ČIŠĆENJE
# ----------------------------------------
cap.release()
cv2.destroyAllWindows()
