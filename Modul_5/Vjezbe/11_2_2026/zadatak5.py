import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist

# ==========================
# EAR funkcija
# ==========================
def calculate_ear(eye_landmarks):
    # vertikalne udaljenosti
    A = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
    B = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
    # horizontalna udaljenost
    C = dist.euclidean(eye_landmarks[0], eye_landmarks[3])

    ear = (A + B) / (2.0 * C)
    return ear


# ==========================
# MediaPipe inicijalizacija
# ==========================
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# EAR parametri
EAR_THRESHOLD = 0.23      # prag zatvorenog oka
CONSEC_FRAMES = 3         # broj uzastopnih frameova

blink_counter = 0
frame_counter = 0

# Indeksi landmarka očiju (MediaPipe Face Mesh)
LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

    while True:
        success, frame = cap.read()
        if not success:
            break

        h, w, _ = frame.shape

        # BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                # Ekstrakcija koordinata očiju
                left_eye = []
                right_eye = []

                for idx in LEFT_EYE_IDX:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    left_eye.append((x, y))

                for idx in RIGHT_EYE_IDX:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    right_eye.append((x, y))

                left_eye = np.array(left_eye)
                right_eye = np.array(right_eye)

                # Izračun EAR
                leftEAR = calculate_ear(left_eye)
                rightEAR = calculate_ear(right_eye)
                ear = (leftEAR + rightEAR) / 2.0

                # Iscrtavanje očiju
                cv2.polylines(frame, [left_eye], True, (0,255,0), 1)
                cv2.polylines(frame, [right_eye], True, (0,255,0), 1)

                # Detekcija treptaja
                if ear < EAR_THRESHOLD:
                    frame_counter += 1
                else:
                    if frame_counter >= CONSEC_FRAMES:
                        blink_counter += 1
                    frame_counter = 0

                # Prikaz EAR i treptaja
                cv2.putText(frame, f"EAR: {ear:.2f}",
                            (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0,255,0), 2)

                cv2.putText(frame, f"Blinks: {blink_counter}",
                            (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0,255,0), 2)

        cv2.imshow("EAR Blink Detection", cv2.flip(frame, 1))

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()