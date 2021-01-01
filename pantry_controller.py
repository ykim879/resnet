import os
import cv2
import numpy as np
 # function that handles the mousclicks
def process_click(event, x, y,flags,param):
     # check if the click is within the dimensions of the button
    button = param
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > button[0] and y < button[1] and x > button[2] and x < button[3]: 
            print("button clicked")
            CameraController()
def process_click_camera(event, x, y,flags,param):
     # check if the click is within the dimensions of the button
    button = param
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > button[0] and y < button[1] and x > button[2] and x < button[3]: 
            param[4] = True #this is clicked
            cv2.destroyAllWindows()
            
class PantryController():
    def __init__(self):
        if len(os.listdir('pantry')) == 0:
            button = [20,60,50,250]
            # create a window and attach a mousecallback and a trackbar
            cv2.namedWindow('Empty Pantry')
            cv2.setMouseCallback('Empty Pantry', process_click, button)
            # create button image
            control_image = np.zeros((160,600), np.uint8)
            control_image[button[0]:button[1],button[2]:button[3]] = 180
            cv2.putText(control_image, 'The pantyr is empty. You need to upload new picture.'
                        ,(100,200),cv2.FONT_HERSHEY_PLAIN, 2,(0),3)
            cv2.putText(control_image, 'Camera',(100,50),cv2.FONT_HERSHEY_PLAIN, 2,(0),3)
            #show 'control panel'
            cv2.imshow('Empty Pantry', control_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:    
            print("Directory is not empty")
class CameraController():
    def __init__(self):
        clicked = False
        button = [20,60,50,250, clicked]
        
        camera = cv2.VideoCapture(0)
        cv2.namedWindow('Take a picture of your pantry!')
        cv2.setMouseCallback('Take a picture of your pantry!', process_click_camera)
        success, frame = camera.read()
        while cv2.waitKey(1) == -1 and not clicked:
            if frame is not None: 
                frame[button[0]:button[1],button[2]:button[3]] = 180
                cv2.putText(frame, 'Take a picture!',(100,50),cv2.FONT_HERSHEY_PLAIN, 2,(0),3)
                cv2.imshow('Take a picture of your pantry!', frame)
            success, frame = camera.read()
        cv2.destroyAllWindows()

pantry = PantryController()