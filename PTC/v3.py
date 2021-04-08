"""
This program can identify only one person.
"""
import numpy as np
import face_recognition as fr
import os
import cv2
import pathlib
import sys
import time
video_capture = cv2.VideoCapture(0)

#welcome message
username = input("Hello, please enter your username:")
time.sleep(1)
print('Welcome, '+ username)
time.sleep(1)
picture = input('What is the original picture called? Please make sure you add the full file name!\nType here:')
time.sleep(1)
picture_exist = pathlib.Path(picture)
if picture_exist.exists ():
    print("Picture Found" + "\nYou can press Q at all time to stop the program")
    time.sleep(1)
    print('Inilizing program')
    time.sleep(2)
else:
    print("Picture not found")
    sys.exit()

#Check if user's webcam is working
if not video_capture.isOpened():
    print('Unable to open camera')
    sys.exit()

image = fr.load_image_file(picture)
face_encoding = fr.face_encodings(image)[0]

known_face_encondings = [face_encoding]
known_face_names = [username]

while True: 
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)   
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = fr.compare_faces(known_face_encondings, face_encoding)

        name = "Unknown"

        face_distances = fr.face_distance(known_face_encondings, face_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Facial Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()