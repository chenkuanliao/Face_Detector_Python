import cv2
from random import randrange
from os import system, name, listdir
from os.path import isfile, join


def Run_Image_Face_Detector():
    # loading some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    onlyfiles = [f for f in listdir('images/') if isfile(join('images/', f))]

    while True:
        print('------------------------------------------------')
        for file in onlyfiles:
            print(f"{onlyfiles.index(file)} {file}")
        print('------------------------------------------------\n')

        print('Please enter a number that corresponds to the image you want to detect')
        print('(Enter q or Q to exit)')

        value = input()

        if value == 'q' or value == 'Q':
            print('Leaving Image Face Detection Mode ...')
            return

        if value.isnumeric() and int(value) < len(onlyfiles) and int(value) >= 0:
            print(f"You have selected the image, {onlyfiles[int(value)]}, to be detected ...")

            # choose an image to detect faces in
            img = cv2.imread('images/' + onlyfiles[int(value)])

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
            cv2.imshow('Image Face Detector', img)

            # wait until a key is pressed
            print('Press any key to close image')
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
        else:
            print('\n!! Invalid Input !!\n')
    
def Run_WebCam_Face_Detector():
    # loading some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    print('Opening your default WebCam ...')

    print('Press any key to exit')

    # capture video from webcam
    webcam = cv2.VideoCapture(0)

    # iterate forever over frames
    while True:
        # read the current frame
        successful_frame_read, frame = webcam.read()

        # converting the image to grayscale => for the sake of using haar cascade algorithm
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        # draw rectangles around the faces
        for coordinates in face_coordinates:
            # getting the coordinates
            (x, y, w, h) = coordinates
            cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 3)

        # showing the image
        cv2.imshow('Clever Programmer Face Detector', frame)

        # wait until a key is pressed
        key = cv2.waitKey(1)

        # stop if Q key is pressed
        if key != -1:
            cv2.destroyAllWindows()
            print('Leaving WebCam Face Detection Mode ...')
            # release the videoCapture object
            webcam.release()
            break

    return

if name == 'nt':
    _ = system('cls')

while True:
    print('\nPlease enter:')
    print('       0 to exit')
    print('       1 for Image Face Detection Mode')
    print('       2 for WebCam Face Detection Mode')
    
    value = input()

    if value == '0':
        print("Code Completed")
        break

    elif value == '1':
        print('Entered Image Face Detection Mode ...')
        Run_Image_Face_Detector()
        print()
    
    elif value == '2':
        print('Entered WebCam Face Detection Mode ...')
        Run_WebCam_Face_Detector()
        print()
    
    else:
        print('\n!!Please enter a valid input!!\n')