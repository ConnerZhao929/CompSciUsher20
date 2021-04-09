"""
This program can identify only one person.
"""
from pathlib import Path
from typing import Any, Union

import numpy as np
import face_recognition as fr
import cv2
import pathlib
import sys

video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print('Unable to access camera')
    sys.exit()

username = input("Hello, please enter your username:")
print('Welcome, ' + username)
picture = input('What is the original picture called? Please make sure you add the full file name!\nType here:')
picture_exist = pathlib.Path(picture)
if picture_exist.exists():
    print("Picture Found")
else:
    print("Picture not found")
while picture_exist.exists() == False:
    return_value, image = video_capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        existBool = True
        picture = (username + '.jpg')
        print(picture)
        cv2.imwrite(picture, image)
        break
video_capture.release()
cv2.destroyAllWindows()

