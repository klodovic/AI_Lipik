import cv2
import numpy as np

# ----------------------------------------
# POSTAVKE
# ----------------------------------------
VIDEO_PATH = "video/primjer_6.mp4"   # promijeni po potrebi

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise SystemExit("Ne mogu otvoriti video datoteku.")

# parametri za detekciju točaka (kutova)
feature_params = dict(
    maxCorners=200,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7
)

# parametri za Lucas–Kanade optical flow
lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

# ----------------------------------------
# 1) UČITAJ PRVI FRAME I NAĐI TOČKE
# ----------------------------------------
ret, old_frame = cap.read()
if not ret:
    raise SystemExit("Ne mogu pročitati prvi frame iz videa.")

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# pronađi točke za praćenje na prvom frameu
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# maska za crtanje trajektorija (posebni sloj preko framea)
mask = np.zeros_like(old_frame)

win_name = "Optički tok (Lucas–Kanade)"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win_name, 960, 540)

# ----------------------------------------
# GLAVNA PETLJA
# ----------------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ako nemamo točke (npr. nakon resetiranja), preskoči optical flow
    if p0 is not None and len(p0) > 0:
        # izračunaj optički tok za prethodne točke p0
        p1, st, err = cv2.calcOpticalFlowPyrLK(
            old_gray, frame_gray, p0, None, **lk_params
        )

        if p1 is not None:
            # zadrži samo točke za koje je tracking uspio (st == 1)
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # iscrtaj linije (staro->novo) i točke na novim pozicijama
            for (new, old) in zip(good_new, good_old):
                a, b = new.ravel()
                c, d = old.ravel()
                a, b, c, d = int(a), int(b), int(c), int(d)

                # linija trajektorije
                cv2.line(mask, (c, d), (a, b), (0, 255, 0), 2)
                # točka na novoj poziciji
                cv2.circle(frame, (a, b), 3, (0, 0, 255), -1)

            # kombiniraj originalni frame i masku s trajektorijama
            output = cv2.add(frame, mask)

            # priprema za sljedeći korak
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1, 1, 2)
        else:
            output = frame.copy()
    else:
        # ako nemamo točke, samo prikaži frame
        output = frame.copy()

    cv2.imshow(win_name, output)

    key = cv2.waitKey(30) & 0xFF
    if key == 113:   # 'q' za izlaz
        break
    if key == 114:   # 'r' za reset točaka (re-detekcija)
        mask[:] = 0
        old_gray = frame_gray.copy()
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

cap.release()
cv2.destroyAllWindows()
