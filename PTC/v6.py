import numpy as np
import face_recognition as fr
import cv2
import pathlib
import sys
import os
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print('Unable to access camera')
    sys.exit()
username = input("Hello, please enter your username:")
print('Welcome, ' + username)

picture = input('Picture Name')
picture_exist = pathlib.Path(picture)
if picture_exist.exists():
    print("Picture Found")
else:
    print("Picture not found")
while True != picture_exist.exists():
    return_value, image = video_capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        existBool = True
        picture = (username + '.jpg')
        print(picture)
        cv2.imwrite(picture, image)
        break

def get_encoded_faces():
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

faces = get_encoded_faces()
known_face_enconding = list(faces.values())
known_face_names = list(faces.keys())

print(known_face_enconding)
print(known_face_names)
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

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    cv2.imshow('Facial Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()