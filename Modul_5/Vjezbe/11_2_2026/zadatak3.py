import cv2
import mediapipe as mp
from numpy.array_api import flip

# Inicijalizacija MediaPipe modula
mp_face_detection = mp.solutions.face_detection

# Otvaranje web kamere
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Web kamera se ne može otvoriti.")

with mp_face_detection.FaceDetection(
        model_selection=0,  # 0 = bliska udaljenost (webcam)
        min_detection_confidence=0.5) as face_detection:

    while True:
        success, frame = cap.read()
        if not success:
            print("Greška pri čitanju frame-a.")
            break

        # Konverzija BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detekcija
        results = face_detection.process(rgb_frame)

        h, w, _ = frame.shape

        if results.detections:
            for detection in results.detections:

                # Confidence score
                confidence = detection.score[0]

                # Bounding box (relativne koordinate → apsolutne)
                bbox = detection.location_data.relative_bounding_box
                x_min = int(bbox.xmin * w)
                y_min = int(bbox.ymin * h)
                box_width = int(bbox.width * w)
                box_height = int(bbox.height * h)

                # Iscrtavanje pravokutnika
                cv2.rectangle(frame,
                              (x_min, y_min),
                              (x_min + box_width, y_min + box_height),
                              (0, 255, 0),
                              2)

                # Tekst pouzdanosti iznad bounding boxa
                text = f"{confidence:.2f}"
                cv2.putText(frame,
                            text,
                            (x_min, y_min - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 0),
                            2)

        # Prikaz (selfie efekt)
        cv2.imshow("Face Detection - Real Time", cv2.flip(frame, 1))

        # ESC za izlaz
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()