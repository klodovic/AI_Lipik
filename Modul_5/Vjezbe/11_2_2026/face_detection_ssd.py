import cv2
import numpy as np
import imutils

prototxt_path = 'models/deploy.prototxt'
caffemodel_path = 'models/res10_300x300_ssd_iter_140000.caffemodel'

print("Loading Face Detector...")
net = cv2.dnn.readNet(caffemodel_path, prototxt_path)

image = cv2.imread("img/slika6.jpg")
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

net.setInput(blob)
detections = net.forward()

confidenceTH = 0.15

for i in range(0, detections.shape[2]):
    
    confidence = detections[0, 0, i, 2]
    
    if confidence < confidenceTH:
        continue
    
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")
    text = "{:.2f}%".format(confidence * 100)
    y = startY - 10 if startY - 10 > 10 else startY + 10
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 220, 255), 2)
    cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 220, 255), 1)
    
# show the output image with the face detections + facial landmarks
cv2.imwrite("Output6.png", image)
#cv2.waitKey(0)