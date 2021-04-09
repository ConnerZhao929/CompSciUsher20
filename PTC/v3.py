"""
This program can identify only one person.
"""
import numpy as np
import face_recognition as fr
import cv2
import pathlib
import sys
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print('Unable to access camera')
    sys.exit()

def init():
    username = input("Hello, please enter your username:")
    print('Welcome, '+ username)
    picture = input('What is the original picture called? Please make sure you add the full file name!\nType here:')
    picture_exist = pathlib.Path(picture)
    if picture_exist.exists():
        print("Picture Found")
    else:
        print("Picture not found")
        sys.exit()
    global username
    global picture
init()

image = fr.load_image_file(picture)
face_encoding = fr.face_encodings(image)[0]
known_face_enconding = [face_encoding]
known_face_names = [username]

print("You can press Q at all time to stop the program")
print('Initializing program')

while True: 
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)   
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = fr.compare_faces(known_face_enconding, face_encoding)

        name = "Unknown"

        face_distances = fr.face_distance(known_face_enconding, face_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    cv2.imshow('Facial Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()