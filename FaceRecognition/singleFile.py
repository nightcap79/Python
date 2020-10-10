import cv2
import numpy as np
import face_recognition


filename = "Assets\962799543203-1351008979.jpg"
filename2 = "Assets\IMG-20181024-WA0005.jpg"
#cap = cv2.VideoCapture(filename)
#cap.open(filename)
# image = face_recognition.load_image_file('ZOZ.jpg')
imageO = cv2.imread(filename2,0)
imageTestO = cv2.imread(filename,0)

image = cv2.cvtColor(imageO, cv2.COLOR_BGR2RGB)
imageTest = cv2.cvtColor(imageTestO, cv2.COLOR_BGR2RGB)


faceLocs = face_recognition.face_locations(image) #return: A list of tuples of found face locations in css (top, right, bottom, left) order
encodeZOoz = face_recognition.face_encodings(image)[1]
encodeTest = face_recognition.face_encodings(imageTest)[0]
x = 0
people = ['Hamed','Khaled','Ali','Rema','Lana','Yanal','Zozo']
for faceLoc in faceLocs:
    cv2.rectangle(image,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,0),1)
    cv2.putText(image,f'{people[x]}', (faceLoc[3],faceLoc[0]), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    x+=1
result = face_recognition.compare_faces([encodeZOoz],encodeTest)

print(result)

cv2.imshow("Group",image)

cv2.waitKey(0)
cv2.destroyAllWindows()



