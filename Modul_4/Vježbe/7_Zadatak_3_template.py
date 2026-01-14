import cv2
import numpy as np

# ----------------------------------------
# UČITAVANJE VIDEA
# ----------------------------------------
cap = cv2.VideoCapture('video/primjer_5.mp4')
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # očekivano 1920
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # očekivano 1080

if not cap.isOpened():
    raise SystemExit("Ne mogu otvoriti video datoteku.")

# ----------------------------------------
# DEFINICIJA OPENCV TRACKERA
# ----------------------------------------
trackers_fcn = [
    cv2.legacy.TrackerBoosting_create,
    cv2.legacy.TrackerMIL_create,
    cv2.legacy.TrackerKCF_create,
    cv2.legacy.TrackerTLD_create,
    cv2.legacy.TrackerMedianFlow_create,
    cv2.legacy.TrackerMOSSE_create,
    cv2.legacy.TrackerCSRT_create
]

track_id = input(
    "Odaberi tracker: \n"
    "0 - Boosting\n"
    "1 - MIL\n"
    "2 - KCF\n"
    "3 - TLD\n"
    "4 - MEDIANFLOW\n"
    "5 - MOSSE\n"
    "6 - CSRT\n"
)

print("\nOdabrano:", track_id)

try:
    track_id = int(track_id)
except ValueError:
    print("Pogrešan unos, izlaz iz programa.")
    exit()

if track_id < 0 or track_id > 6:
    print("Neispravan ID trackera, koristim CSRT (6).")
    track_id = 6

# ----------------------------------------
# POČETNI ODABIR OBJEKTA (ROI)
# ----------------------------------------
ret, frame = cap.read()
if not ret:
    raise SystemExit("Ne mogu pročitati prvi frame iz videa.")

# odabir ROI-a u posebnom prozoru
rois = []
print("\nOznači prvi ROI, zatim pritisni ENTER.")
print("Za prekid odabira pritisni ESC u prozoru za odabir.\n")

while True:
    roi = cv2.selectROI("Odaberi objekt", frame, fromCenter=False, showCrosshair=True)

    if roi == (0, 0, 0, 0): #ESC
        print("Završen odabir ROI-eva.\n")
        break

    rois.append(roi)
    print("Novi ROI je dodan!", roi)
    cv2.destroyWindow("Odaberi objekt")


if len(rois) == 0:
    raise SystemExit("Nema odabranih ROI - prekid programa!")
cv2.destroyAllWindows()

# ----------------------------------------
# STVARANJE I INICIJALIZACIJA TRACKERA
# ----------------------------------------
trackers = []
# colors = []

for i, roi in enumerate(rois):
    tracker = trackers_fcn[track_id]()
    tracker.init(frame, roi)
    trackers.append(tracker)

    # color = (np.random.randint(50,255), np.random.randint(50,255), np.random.randint(50,255))
    # colors.append(color)

print(f"Ukupno trackera:{len(trackers)}")

# ----------------------------------------
# PRIPREMA PROZORA ZA PRIKAZ
# ----------------------------------------
win_name = 'Tracking'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# prozor postavi u gornji lijevi kut PRIMARNOG monitora
cv2.moveWindow(win_name, 0, 0)

# opcionalno: postavi veličinu prozora jednaku veličini videa
cv2.resizeWindow(win_name, width, height)

# ----------------------------------------
# GLAVNA PETLJA – PRAĆENJE OBJEKTA
# ----------------------------------------
while True:

    ret, frame = cap.read()
    if not ret:
        break  # kraj videa

    
    for i, tracker in enumerate(trackers):
        ok, bbox = tracker.update(frame)

        if ok:
            x, y, w, h = [int(v) for v in bbox]
            p1 = (x, y)
            p2 = (x + w, y + h)
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            cv2.putText(
                frame,
                "Tracking OK",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 0),
                2
            )
        else:
            cv2.putText(
                frame,
                "Tracking failure!",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 0, 255),
                2
            )

    cv2.imshow(win_name, frame)

    key = cv2.waitKey(1) & 0xff
    if key == 113:          # 'q'
        break

cap.release()
cv2.destroyAllWindows()




