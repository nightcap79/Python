import cv2

filename = "M2U00004.MPG"

cap = cv2.VideoCapture(filename)

cap.open(filename)

cap.imshow()