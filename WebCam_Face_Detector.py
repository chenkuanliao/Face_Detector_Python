import cv2
from random import randrange
import os
import time
import keyboard

# def Run_Image_Face_Detector():
#     # loading some pre-trained data on face frontals from opencv (haar cascade algorithm)
#     trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#     # choose an image to detect faces in
#     img = cv2.imread('images/' + '2friends.png')

#     # converting the image to grayscale => for the sake of using haar cascade algorithm
#     grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # detect faces
#     face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#     # draw rectangles around the faces
#     for coordinates in face_coordinates:
#         # getting the coordinates
#         (x, y, w, h) = coordinates
#         cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 3)

#     # showing the image
#     cv2.imshow('Image Face Detector', img)

#     # wait until a key is pressed
#     cv2.waitKey()

# def Run_WebCam_Face_Detector():

# print('Opening your default WebCam ...')

# print('Press q or Q key to exit')

#     # capture video from webcam
#     webcam = cv2.VideoCapture(0)

#     # iterate forever over frames
#     while True:
#         # read the current frame
#         successful_frame_read, frame = webcam.read()

#         # converting the image to grayscale => for the sake of using haar cascade algorithm
#         grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # detect faces
#         face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#         # draw rectangles around the faces
#         for coordinates in face_coordinates:
#             # getting the coordinates
#             (x, y, w, h) = coordinates
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 3)

#         # showing the image
#         cv2.imshow('Clever Programmer Face Detector', frame)

#         # wait until a key is pressed
#         key = cv2.waitKey(1)

#         # stop if Q key is pressed
#         if key == 81 or key == 113:
#             break


#     # release the videoCapture object
#     webcam.release()