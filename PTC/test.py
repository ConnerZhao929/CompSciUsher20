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

#welcome message
username = input("Enter username:")
print('Welcome, '+ username)

#checks if the user have any images in the folder
path = "./faces"
dir = os.listdir(path) 
if len(dir) == 0: 
    sys.exit("No faces are detected in folder.")
else: 
    print("Faces detected")

#Encodes the Faces the User inputs in the folder.
def get_encoded_faces(): 
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"): #Takes pictures in faces and 
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Locate all the faces and face encoding from the gather image(webcam).
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check faces(Comparing).
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            #if the faces are unknown, they are labled "Unknown"
            name = "Unknown"

            # # If a match was found in faces_encoded, just use the first one.
            if True in matches:
                 first_match_index = matches.index(True)
                 name = known_face_names[first_match_index]
            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)