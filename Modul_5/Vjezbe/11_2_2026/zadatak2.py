import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection

# Učitavanje slike
image = cv2.imread("img/barcelona.jpg")
if image is None:
    raise SystemExit("Slika nije pronađena!")
h, w, _ = image.shape

# Ručna inicijalizacija (bez with)
face_detection = mp_face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.3
)

# MediaPipe koristi RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = face_detection.process(rgb)
if results.detections:
    for detection in results.detections:
        confidence = detection.score[0]
        bbox = detection.location_data.relative_bounding_box
        x = int(bbox.xmin * w)
        y = int(bbox.ymin * h)
        bw = int(bbox.width * w)
        bh = int(bbox.height * h)
        cv2.rectangle(image, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
        text = f"{confidence:.2f}"
        cv2.putText(image, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)
else:
    print("Nema detektiranih lica.")

# Oslobađanje resursa (bitno kad ne koristiš with)
face_detection.close()

cv2.imshow("Detekcija lica", image)
cv2.waitKey(0)
cv2.destroyAllWindows()