import cv2# Import the OpenCV library
import os

cap = cv2.VideoCapture(0)# Create a VideoCapture object for the default camera (index 0)
cap.set(3,640)# Set the width of the captured frames to 640 pixels
cap.set(4,480)# Set the height of the captured frames to 480 pixels

Backgroundimg = cv2.imread('Resources/Background.png')#the variable image background stores the data from the image it reads at a specific directory

cv2_imread_modes=[]#stores a list of images with each individual pixel data
path = "Resources/Modes"#path to find modes in file
dir_list = os.listdir(path)# Retrieve a list of all png's (files and directories) present in the specified directory path

for i in dir_list:#for each element in dir_list I apply the cv2.imread function to collect pixel data of each image
    cv2_imread_modes.append(cv2.imread((str(path+'/'+i))))#appends the pixel data of each image into a list named cv2_imread_modes 
                            #the bracket here creates the directory of the image


while True:
    
    capture_success, webcam = cap.read()#'cap.read()'->captures a frame from the camera returning a tuple constaining 2 values. A boolean stored within "capture_success" and an image stored in "img" 

    Backgroundimg[162:162+480,55:55+640] = webcam # Replaces a specific region of Backgroundimg with the image captured from the webcam.
    #The replaced region starts 162 pixels down and 55 pixels across from the top-left corner of Backgroundimg.The replaced region covers a height of 480 pixels and a width of 640 pixels.
    Backgroundimg[44:44+633,808:808+414] = cv2_imread_modes[1]#Replaces a specifc region of backgroundimg with the mode which has a heigh of 633 and wdth of 414 pixels
    #cv2.imshow("webcam",img)#displays the img captured previously on an application titled "Face_Attendance_System"
    
    cv2.imshow("Face_Attendance_system", Backgroundimg)#displays the background img every frame

    cv2.waitKey(1) # introduce a delay between each displayed frame in OpenCV. with a 1ms dealy
    
    if cv2.waitKey(1) & 0xFF == ord("q"):#if a key is pressed and it has the ASCII value 'q' the program breaks
        break 