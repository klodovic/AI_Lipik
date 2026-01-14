import cv2

video_path = "moving_objects.mp4"
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

    cv2.imshow("Original image", frame)
    cv2.imshow("MOG", mask_mog)
    cv2.imshow("MOG2 shadow flase", mask_mog2_shadow_false)
    cv2.imshow("MOG2 shadow true", mask_mog2_shadow_true)

    if cv2.waitKey(0) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

