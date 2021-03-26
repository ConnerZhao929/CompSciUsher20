#imports the Facial recognition modules as fr for simplicity reasons
import face_recognition as fr
#imports the Miscellaneous operating system interfaces
import os
#imported openCV
import cv2
#imported Facial Recognition
import face_recognition
#imported Numeric Python module
import numpy as np
from time import sleep


def get_encoded_faces():
    #This utilizes the facial_recognition module and encodes the face in the folder with its name accordingly.
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"): #Takes pictures in faces
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
                #encodes the faces as encoding
    return encoded


def unknown_image_encoded(img):
    #This utilizes the facial_recognition module and encodes the unknown faces.
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    This will find all of the faces in a given image and label
    And ouput if the face is known or not.
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    # Utilizes the face_recognition.face_locations() feature to locate the images
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # Utilizes the face_recognition.compare_faces() feature to compare faces in the test.jpg
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # Utilizes the face_recognition.face_distance() feature to compare known face with the smallest distance to the new face 
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        print(face_names)


print(classify_face("test.jpg"))


