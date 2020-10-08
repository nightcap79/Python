import cv2
import numpy as np
import face_recognition


filename = "Assets\ZOZ.jpg"

#cap = cv2.VideoCapture(filename)
#cap.open(filename)
# image = face_recognition.load_image_file('ZOZ.jpg')
image = cv2.imread(filename,0)
print(image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("test",image)
cv2.waitKey(0)



