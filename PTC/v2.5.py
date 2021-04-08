#imports the Facial recognition modules as fr for simplicity reasons
import face_recognition as fr
#imports the Miscellaneous operating system interfaces
import os
from os import path
import pathlib
from pathlib import Path
#imported openCV
import cv2
video_capture = cv2.VideoCapture(0)
#imported Facial Recognition
import face_recognition
#imported Numeric Python module
import numpy as np
from time import sleep
import sys

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces
    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

#welcome message
username = input("Enter username:")
print('Welcome, '+ username)

#Checks if the user have any images in the folder
path = "./faces"
dir = os.listdir(path) 
if len(dir) == 0: 
    print("No faces are detected in folder.")
    sys.exit()
else: 
    print("Faces detected")

#Check if user's webcam is working
if not video_capture.isOpened():
    print('Unable to open camera')
    sys.exit()

#Encodes the Faces the User inputs in the folder.

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    ret, frame = video_capture.read()

    rgb_small_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
             name = known_face_names[best_match_index]

        face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()