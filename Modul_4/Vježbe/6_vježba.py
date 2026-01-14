import cv2
import numpy as np

# zadatak 1

"""
Prepiši i pokreni kod iz skripte primjeri/primjer_1_oduzimanje_pozadine.py.
● Usporedi rezultate MOG i MOG2: promijeni inicijalizaciju 
(MOG → cv2.bgsegm.createBackgroundSubtractorMOG(), MOG2 → cv2.createBackgroundSubtractorMOG2()); 
prikaži maske i video izlaz.
● Za MOG2 isprobaj detectShadows=True i detectShadows=False; opiši što se mijenja u maski (npr. sive sjene vs. čisti fg).
● Kako biste se riješili sjena?
"""

video_path = "img/nadzor_autoceste.mp4"
cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    print(f"Cannot open video: {video_path}")
    exit(1)

mog = cv2.bgsegm.createBackgroundSubtractorMOG()
mog2_shadow_false = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
mog2_shadow_true = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # MOG
    mask_mog = mog.apply(frame)

    # MOG2
    mask_mog2_shadow_false = mog2_shadow_false.apply(frame)
    mask_mog2_shadow_true = mog2_shadow_true.apply(frame)

    # cv2.imshow("Original image", frame)
    # cv2.imshow("MOG", mask_mog)
    # cv2.imshow("MOG2 shadow flase", mask_mog2_shadow_false)
    # cv2.imshow("MOG2 shadow true", mask_mog2_shadow_true)

    if cv2.waitKey(0) == ord("q"):
        break

# cap.release()
# cv2.destroyAllWindows()


# zadatak 2
"""
Metodom oduzimanja pozadine implementirajte jednostavan sustav za praćenje gužve na autocestama.
Upute:
● Koristite dani video zadaci/oduzimanje_pozadine/nadzor_autoceste.mp4 i algoritam MOG2 za izdvajanje pokretnih objekata.
● Nakon segmentacije očistite masku morfološkim operacijama, zatim je binarizirajte pragom (npr. odbacite sve piksele slabijeg intenziteta od npr 200) kako biste uklonili sjene/slabe odgovore.
● Pronađite konture većih objekata, postavite pravokutnike oko njih i ispišite broj detektiranih vozila u svakom kadru.
● Omogućite prikaz izvornog kadra, maske oduzimanja pozadine, binarizirane maske i anotiranog kadra, te prekid rada pritiskom na tipku q.
● Skriptom demonstrirajte kako
"""

import cv2
import numpy as np

video_path = "img/nadzor_autoceste.mp4"
cap = cv2.VideoCapture(str(video_path))
mog2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # za morfološke operacije - uklnanjanje šuma

# petlja za obradu videa (frame by frame)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    fg_mask = mog2.apply(frame) # primjena MOG2 za dobivanje maske prednjeg plana
    _, binary_mask = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY) # binarizacija maske
    cleaned_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel) # uklanjanje šuma
    cleaned_mask2 = cv2.dilate(cleaned_mask, kernel=kernel)

    contours, _ = cv2.findContours(cleaned_mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # pronalaženje kontura
    
    vehicle_count = 0
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # filtriranje kontura manjih od 500 piksela
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # crtanje pravokutnika oko detektiranih vozila
            vehicle_count += 1

    cv2.putText(frame, f'Vehicles: {vehicle_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) # ispis broja vozila na frame

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Foreground Mask", fg_mask)
    cv2.imshow("Binary Mask", binary_mask)
    cv2.imshow("Cleaned Mask", cleaned_mask)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break   
cap.release()
cv2.destroyAllWindows()






