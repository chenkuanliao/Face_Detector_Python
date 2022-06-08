import imp
import cv2
from random import randrange

# loading some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect faces in
# img = cv2.imread('RDJ.png')
img = cv2.imread('2friends.png')

# converting the image to grayscale => for the sake of using haar cascade algorithm
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# draw rectangles around the faces
for coordinates in face_coordinates:
    # getting the coordinates
    (x, y, w, h) = coordinates
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 3)

# showing the image
cv2.imshow('Clever Programmer Face Detector', img)

# wait until a key is pressed
cv2.waitKey()











print("Code Completed")