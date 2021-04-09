import cv2
import os
video_capture = cv2.VideoCapture(0)
username = input('username:')
directory = os.getcwd()
path = (directory + ('/faces/'))
print(path)

while True:
    return_value, image = video_capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        existBool = True
        picture = (username + '.jpg')
        print(picture)
        cv2.imwrite(path + picture, image)
        break
video_capture.release()
cv2.destroyAllWindows()
