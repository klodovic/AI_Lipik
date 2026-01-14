import cv2
import numpy as np


# read images
query_img_bgr = cv2.imread('img/znak.png')
train_img_bgr = cv2.imread('img/ulica.png')

# convert to grayscale
query_img_gray = cv2.cvtColor(query_img_bgr, cv2.COLOR_BGR2GRAY)
train_img_gray = cv2.cvtColor(train_img_bgr, cv2.COLOR_BGR2GRAY)

# initialize SIFT detector 
sift = cv2.SIFT_create()

# find the keypoints and descriptors with SIFT
kp_query, desc_queary = sift.detectAndCompute(query_img_gray, None)
kp_train, desc_train = sift.detectAndCompute(train_img_gray, None)

img_query_kp = cv2.drawKeypoints(query_img_bgr, kp_query, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img_train_kp = cv2.drawKeypoints(train_img_bgr, kp_train, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# cv2.imshow('Query Image Keypoints', img_query_kp)
# cv2.imshow('Train Image Keypoints', img_train_kp)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# create BFMatcher object
bf = cv2.BFMatcher()
# match descriptors
matches = bf.knnMatch(desc_queary, desc_train, k=2)

# apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
# draw matches
img_matches = cv2.drawMatches(query_img_bgr, 
                              kp_query, 
                              train_img_bgr, 
                              kp_train, 
                              good_matches, 
                              None, 
                              flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# show matches
# cv2.imshow('Good Matches', img_matches)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if len(good_matches) >= 5:
    # extract location of good matches
    src_pts = np.float32([kp_query[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp_train[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # compute homography
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

    if M is not None:
        # get dimensions of query image
        h, w = query_img_gray.shape
        # define corners of the query image
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        # project corners into train image
        dst = cv2.perspectiveTransform(pts, M)

        # draw projected corners on train image
        train_img_bgr = cv2.polylines(train_img_bgr, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)

        # show detected object
        cv2.imshow('Detected Object', train_img_bgr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Not enough good matches found - {}/{}".format(len(good_matches), 5))     

















