import cv2
import numpy as np
import face_recognition


filename = "Assets\All_faces.jpg"
filename2 = "Assets\IMG-20181024-WA0007.jpg"
#cap = cv2.VideoCapture(filename)
#cap.open(filename)
# image = face_recognition.load_image_file('ZOZ.jpg')

image = cv2.imread(filename,-1)
imageTest = cv2.imread(filename2,-1)

if image is None:
    file = filename.split('\\')[1]
    print(f"Image {file} not found")
    quit()

if  imageTest is None:
    file = filename2.split('\\')[1]
    print(f"Image {file} not found")
    quit()

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# imageTest = cv2.cvtColor(imageTest, cv2.COLOR_BGR2RGB)


know_face_locations = face_recognition.face_locations(image) #return: A list of tuples of found face locations in css (top, right, bottom, left) order
known_face_encodings = face_recognition.face_encodings(image)

x = 0
people = ['Hamed','Khaled','Rema','Ali','Lana','Zozo','Yanal']
for faceLoc in know_face_locations:
    img = image [faceLoc[0]: faceLoc[2],faceLoc[3]:faceLoc[1] ]
    cv2.imwrite(f'Assets\Faces\{people[x]}.png', img)
    cv2.rectangle(image,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,0),1)
    cv2.putText(image,f'{people[x]}', (faceLoc[3],faceLoc[0]), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    x+=1
    



faceLocationsTest = face_recognition.face_locations(imageTest) #return: A list of tuples of found face locations in css ( top 0 , right 1 , bottom 2 , left 3 ) order


faces_encoding_to_check = face_recognition.face_encodings(imageTest)[0]


for faceLoc,face_encoding_to_check in zip(faceLocationsTest,faces_encoding_to_check):
    result = face_recognition.compare_faces(known_face_encodings,face_encoding_to_check,0.5)
    np.index_exp(result,True)
    cv2.rectangle(imageTest,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,0),1)
    cv2.putText(imageTest,f'{people[x]}', (faceLoc[3],faceLoc[0]), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

result = face_recognition.compare_faces([encode],encodeTest)

print(result)

cv2.putText(image, "Founded Faces", (30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2,)

cv2.imshow("Faces Found",imageTest)

cv2.waitKey(0)
cv2.destroyAllWindows()



