"""
Izradite aplikaciju za brojanje osoba koje prelaze virtualnu liniju u video snimci iz stacionarne kamere.
Koristite oduzimanje pozadine i morfološke operacije za izdvajanje pokretnih objekata te pronađite njihove
centre (centroid) i pratite ih kroz vrijeme. Kada centroid osobe prijeđe zadanu liniju, povećajte brojač i
odredite smjer prelaska (ulaz/izlaz). Rezultat prikažite kao overlay na videu (trenutni brojači) i spremite
izlazni video.
"""

import cv2
import func as fun


# https://www.pexels.com/video/black-and-white-video-of-people-853889/
video_path = "video_v/ped.mp4"
cap = cv2.VideoCapture(str(video_path))
mog2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

## just to check video properties
# print(f"Frame width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} px")
# print(f"Frame height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)} px")

# calculating properties of the video ans setting line position
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
line_position_y = height // 3

# writer za izlazni video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("video_v/output_pedestrian.avi", fourcc, fps, (width, height))



pedestrian_count_up = 0
pedestrian_count_down = 0
tracks = {}
next_object_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    thresh = 150
    mask_clean = fun.preprocess_mask(mog2, kernel, frame, thresh)
    contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # crtanje linije
    cv2.line(frame, (0, line_position_y), (width, line_position_y), (0, 0, 255), 2)   

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        assigned_id = None # ID object for current contour
        min_distance = 40 # threshold for matching existing objects

        x, y, w, h = cv2.boundingRect(contour)
        center_x, center_y = fun.get_centroid(x, y, w, h)  # coordinates of bounding box center

        assigned_id, next_object_id = fun.match_object(center_x, center_y, tracks, min_distance, assigned_id, next_object_id)

        if assigned_id in tracks: # if we have seen this object before
            prev_cx, prev_cy = tracks[assigned_id]
            # from top to bottom - count pedestrian crossing the line downwards
            if prev_cy < line_position_y and center_y >= line_position_y:
                pedestrian_count_down = fun.pedestrian_count(pedestrian_count_down)
            # from bottom to top - count pedestrian crossing the line upwards
            if prev_cy > line_position_y and center_y <= line_position_y:
                pedestrian_count_up = fun.pedestrian_count(pedestrian_count_up)

        tracks[assigned_id] = (center_x, center_y)

        fun.object_bounding_box(frame, assigned_id, x, y, w, h, center_x, center_y)
    fun.counter_text(pedestrian_count_up, pedestrian_count_down, frame, "Going Up", "Going Down")

    #out.write(frame) # saving output video frame by frame

    cv2.imshow("Original Frame", frame)
    # cv2.imshow("Foreground Mask", fg_mask)
    # cv2.imshow("Binary Mask", binary_mask)
    # cv2.imshow("Cleaned Mask", cleaned_mask)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break   

cap.release()
out.release()
cv2.destroyAllWindows()
