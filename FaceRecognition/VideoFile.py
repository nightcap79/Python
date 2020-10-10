import cv2
import numpy as np
import face_recognition


filename = "Assets\All_faces.jpg"
filename2 = "Assets\iyad.mp4"



# image = face_recognition.load_image_file('ZOZ.jpg')
imageO = cv2.imread(filename,0)
image = cv2.cvtColor(imageO, cv2.COLOR_BGR2RGB)

# imageTestO = cv2.imread(filename2,0)

faceLocs = face_recognition.face_locations(image) #return: A list of tuples of found face locations in css (top, right, bottom, left) order
known_face_encodings = face_recognition.face_encodings(image)


known_face_names = ['Hamed','Khaled','Ali','Rema','Lana','Yanal','Zozo']

# x = 0
# for faceLoc in faceLocs:
#     cv2.rectangle(image,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,0),1)
#     cv2.putText(image,f'{known_face_names[x]}', (faceLoc[3],faceLoc[0]), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
#     x+=1

cap = cv2.VideoCapture(filename2)

while True:
    _, frame  = cap.read()
 
    rgb_frame = frame [:, :, ::-1]  # cv2.cvtColor(imageTestO, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unkown"
        face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        

        cv2.rectangle(frame, (left,top),(right, bottom), (0,0,255),thickness=2  )    
        # cv2.rectangle(frame, (left,bottom -35),(right, bottom), (0,0,255), cv2.FILLED  )    
        cv2.putText(frame, name, (left + 6, bottom - 6),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255),1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
