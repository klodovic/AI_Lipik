import cv2
import numpy as np

# Load the image in grayscale mode
img = cv2.imread("img/houses.jpg") #, cv2.IMREAD_GRAYSCALE

if img is None:
    print("Error: Image not found.")
    exit(1)

print("Image dimensions:", img.shape)
# cv2.imshow("Houses", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Save the grayscale image
cv2.imwrite("img/houses_gray.jpg", img)


# Resize to specific dimensions
new_width = 500
new_height = 700
np.empty((new_height, new_width, 3), dtype=np.uint8)
larger_img = cv2.resize(img, (new_width, new_height)) # dsize is (width, height)
print("Resized image dimensions:", larger_img.shape)
# cv2.imshow("Resized Houses", larger_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Resize using scaling factors
new_img = cv2.resize(img, None, fx=2, fy=2) # dsize= None means that we are using scaling factors, use tuple (width, height) to set exact size
print("Resized image dimensions:", new_img.shape)

# cv2.imshow("Resized Houses", new_img)
# cv2.imshow("Houses", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Flipping the image
flipped_img = cv2.flip(img, 0) # 0 - vertical, 1 - horizontal, -1 - both
# cv2.imshow("Flipped Houses", flipped_img)   
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Partial modification of the image into a specific color
img[:50, :50] = [255, 0, 0]  # Top-left corner to blue
# cv2.imshow("Modified Houses", img)  
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Convert to different color spaces
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convert from BGR to HSV

img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR) # Convert back to BGR to display correctly
# cv2.imshow("Houses HSV", img_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Binarization
chair = cv2.imread("img/chair.png")
gray_img = cv2.cvtColor(chair, cv2.COLOR_BGR2GRAY) # Convert to grayscale for binarization
_ , chair_bin = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY_INV, gray_img) # Apply binary thresholding, # cv.THRESH_BINARY_INV for inverse

rectangle = cv2.boundingRect(chair_bin)
print("Bounding rectangle (x, y, width, height):", rectangle)

cv2.rectangle(chair, rectangle, (0, 255, 0), 2)  # Draw rectangle on original image

# cv2.imshow("Original image", chair)
# #cv2.imshow("Binarized Chair", chair_bin)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Filtering objects based on color
img_road = cv2.imread("img/road.jpg")
img_hsv = cv2.cvtColor(img_road, cv2.COLOR_BGR2HSV)

lower_bound = np.array([150/2, 80, 80])
upper_bound = np.array([176/2, 255, 255])

mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
result = cv2.bitwise_and(img_road, img_road, mask=mask) # Apply mask to original image
# cv2.imshow("Filtered Color", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Blur image
img_houses_bgr = cv2.imread("img/houses.jpg")
# blur, medianBlur, GaussianBlur, bilateralFilter, boxFilter
    # medianBlur - good for removing salt-and-pepper noise, good for edges
    # GaussianBlur - good for general blurring, uses Gaussian kernel
blurred_img = cv2.GaussianBlur(img_houses_bgr, (15, 15), 0) # Apply Gaussian blur, kernel size (15,15) must be odd and positive
# cv2.imshow("Blurred Houses", blurred_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Edge detection - Sobel, Canny

# Sobel
img_houses_bgr = cv2.imread("img/houses.jpg", cv2.IMREAD_GRAYSCALE)
img_houses_bgr_blur = cv2.medianBlur(img_houses_bgr, 7) # Apply median blur to reduce noise

sobel_x = cv2.Sobel(img_houses_bgr_blur, cv2.CV_64F, 1, 0, ksize=5) # Sobel in x direction
sobel_y = cv2.Sobel(img_houses_bgr_blur, cv2.CV_64F, 0, 1, ksize=5) # Sobel in y direction

sobel_x_scaled = cv2.convertScaleAbs(sobel_x) # Convert back to uint8
sobel_y_scaled = cv2.convertScaleAbs(sobel_y) # Convert back to uint8

sobel_combined = cv2.bitwise_or(sobel_x_scaled, sobel_y_scaled) # Combine both directions
# cv2.imshow("Sobel Edge Detection", sobel_combined)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Canny
img_houses_gray = cv2.imread("img/houses.jpg", cv2.IMREAD_GRAYSCALE)
canny_img = cv2.Canny(img_houses_gray, 100, 200) # Apply Canny edge detection with thresholds 100 and 200
cv2.imshow("Canny Edge Detection", canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



























