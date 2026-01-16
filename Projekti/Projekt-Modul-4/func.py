import cv2



def preprocess_mask(mog2, kernel, frame, thresh):

    """
    Generates a cleaned foreground mask from a video frame using background
    subtraction and morphological operations.

    The function first applies the MOG2 background subtractor to extract
    moving objects from the static background. The resulting mask is then
    binarized using a threshold and cleaned using morphological opening to
    remove noise, followed by dilation to connect fragmented object regions.

    :param mog2: Background subtractor instance (cv2.createBackgroundSubtractorMOG2)
    :param kernel: Structuring element used for morphological operations
    :param frame: Input video frame (BGR image)
    :param thresh: Threshold value for binarization of the foreground mask
    :return: Cleaned binary mask containing detected foreground regions
    """

    fg_mask = mog2.apply(frame)
    _, binary_mask = cv2.threshold(fg_mask, thresh, 255, cv2.THRESH_BINARY)
    mask_clean = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)
    mask_clean = cv2.dilate(mask_clean, kernel)
    return mask_clean




def get_centroid(x, y, w, h):

    """
    Calculates the centroid (center point) of a bounding box.

    The bounding box is defined by its top-left corner (x, y) and its
    width (w) and height (h). The centroid is returned as the midpoint
    of the rectangle along both axes.

    :param x: X-coordinate of the top-left corner of the bounding box
    :param y: Y-coordinate of the top-left corner of the bounding box
    :param w: Width of the bounding box in pixels
    :param h: Height of the bounding box in pixels
    :return: (cx, cy) tuple representing the centroid coordinates
    """
    return (x + w // 2, y + h // 2)




def match_object(center_x, center_y, tracks, min_distance, assigned_id, next_object_id):

    """
    Matches the current detected object to an existing tracked object
    based on the distance between centroids. If no suitable match is
    found, a new object ID is assigned.

    The function uses a simple nearest-neighbor approach in centroid space:
    if the distance between the current centroid and a previously tracked
    centroid is smaller than a defined threshold, the object is assumed to
    be the same and its existing ID is reused. Otherwise, a new ID is
    created for a newly detected object.

    :param center_x: X-coordinate of the current object's centroid
    :param center_y: Y-coordinate of the current object's centroid
    :param tracks: Dictionary of tracked objects in the form {object_id: (prev_x, prev_y)}
    :param min_distance: Maximum allowed distance to consider two detections as the same object
    :param assigned_id: Currently assigned object ID (None for new objects)
    :param next_object_id: Next available unique ID for new objects
    :return: (assigned_id, next_object_id) assigned_id – ID matched or newly assigned to the object next_object_id – updated counter for future IDs
    """

    for obj_id, (previous_x, previous_y) in tracks.items(): # check existing objects
        distance = abs(center_x - previous_x) + abs(center_y - previous_y)
        if distance < min_distance:
            assigned_id = obj_id
            next_object_id += 1

    if assigned_id is None: # new object
        assigned_id = next_object_id
        next_object_id += 1
    return assigned_id, next_object_id




def pedestrian_count(pedestrian_count):

    """
    Increments the pedestrian count by one.

    This function is a simple utility to encapsulate the logic of
    counting pedestrians. It takes the current count as input and
    returns the incremented value.

    :param pedestrian_count: Current count of pedestrians
    :return: Updated count of pedestrians after incrementing by one
    """
    pedestrian_count += 1
    return pedestrian_count 




def object_bounding_box(frame, assigned_id, x, y, w, h, center_x, center_y):

    """
    Draws the visual representation of a tracked object on the video frame.

    The function renders a bounding box around the detected object, marks its
    centroid, and displays the object's tracking ID above the bounding box.
    This visual overlay is useful for debugging, visualization of tracking,
    and interpreting object movements in the video output.

    :param frame: Video frame on which the bounding box and labels are drawn
    :param assigned_id: Unique identifier of the tracked object
    :param x: X-coordinate of the top-left corner of the bounding box
    :param y: Y-coordinate of the top-left corner of the bounding box
    :param w: Width of the bounding box in pixels
    :param h: Height of the bounding box in pixels
    :param center_x: X-coordinate of the object's centroid
    :param center_y: Y-coordinate of the object's centroid
    :return: None (the frame is modified in-place)
    """
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)
    cv2.putText(frame, f"ID {assigned_id}", (x, y - 5),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)




def counter_text(pedestrian_count_up, pedestrian_count_down, frame, text_dir_one, text_dir_two):
    """
    Draws the current pedestrian counters on the video frame as overlay text.

    This function displays two counters: the number of people moving upward
    across the virtual line (ENTER) and the number of people moving downward
    (EXIT). The counters are rendered directly onto the frame and are intended
    to be shown in the output video or during live preview.

    :param pedestrian_count_up: Number of pedestrians detected crossing the line in the upward direction
    :param pedestrian_count_down: Number of pedestrians detected crossing the line in the downward direction
    :param frame: Video frame on which the counter text will be drawn
    :return: None (the input frame is modified in-place)
    """
    cv2.putText(frame, f"{text_dir_one}: {pedestrian_count_up}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    cv2.putText(frame, f"{text_dir_two}: {pedestrian_count_down}", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)







