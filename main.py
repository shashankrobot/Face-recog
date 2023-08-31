import cv2# Import the OpenCV library
import os
import pickle
import face_recognition
########################################################################################################################################
cap = cv2.VideoCapture(0)# Create a VideoCapture object for the default camera (index 0)
cap.set(3,640)# Set the width of the captured frames to 640 pixels
cap.set(4,480)# Set the height of the captured frames to 480 pixels

Backgroundimg = cv2.imread('Resources/Background.png')#the variable image background stores the data from the image it reads at a specific directory
########################################################################################################################################
cv2_imread_modes=[]#stores a list of images with each individual pixel data
path = "Resources/Modes"#path to find modes in file
dir_list = os.listdir(path)# Retrieve a list of all png's (files and directories) present in the specified directory path

for i in dir_list:#for each element in dir_list I apply the cv2.imread function to collect pixel data of each image
    cv2_imread_modes.append(cv2.imread((str(path+'/'+i))))#appends the pixel data of each image into a list named cv2_imread_modes 
                            #the bracket here creates the directory of the image
########################################################################################################################################
#Loading the encoded files
file=open('EncodedData.p','rb')#opening the file in binary read mode
encoded_imgs_with_IDs = pickle.load(file)#coppying the array from the file into a variable
file.close()#closing the file
encoded_imgs_output,Ids = encoded_imgs_with_IDs#storing the arrays listed in the file in 2 different variables
#print(Ids)
#print(encoded_imgs_output)
print('Loading encoded Data')
########################################################################################################################################
while True:
    capture_success, webcam = cap.read()#'cap.read()'->captures a frame from the camera returning a tuple constaining 2 values. A boolean stored within "capture_success" and an image stored in "img" 
    #webcams=cv2.resize(webcam ,(0,0),None,0.25,0.25)
    webcams = cv2.cvtColor(webcam, cv2.COLOR_BGR2RGB)#converts the colour of the image read using cv2 library from BGR to RGB
    face_in_cur_frame = face_recognition.face_locations(webcams)#returns a list of tuples representing the face bounidng boxes(topright,topleft,bottomleft,bottomright) in other words the location
    Encoding_Cur_Frame = face_recognition.face_encodings(webcams,face_in_cur_frame)#computes a face encoding for the given image and face locations
########################################################################################################################################
    #setting up the webcam and modes in the background to be seen
    Backgroundimg[162:162+480,55:55+640] = webcam # Replaces a specific region of Backgroundimg with the image captured from the webcam.
    #The replaced region starts 162 pixels down and 55 pixels across from the top-left corner of Backgroundimg.The replaced region covers a height of 480 pixels and a width of 640 pixels.
    Backgroundimg[44:44+633,808:808+414] = cv2_imread_modes[1]#Replaces a specifc region of backgroundimg with the mode which has a heigh of 633 and wdth of 414 pixels
    #cv2.imshow("webcam",img)#displays the img captured previously on an application titled "Face_Attendance_System"
########################################################################################################################################
    #Making a border around any face identified on the webcam



########################################################################################################################################
    #Checking for matching
    for Encoded_Face in (Encoding_Cur_Frame):#iterates through a list of encoded images and compares them to the current encoded frame
        match_found=face_recognition.compare_faces(encoded_imgs_output,Encoded_Face)#compares the face's encoding in the current frame with a list of known encoded faces
        #print(match_found)  # Prints a list of True or False values. Each value corresponds to an element(image) in the list of known images. 
        #True indicates a match (a person's image is found), while False indicates no match.
########################################################################################################################################
    
    #checking for similarity
    for Face in (face_in_cur_frame):#iterates through a list of faces within the captured frame
        face_difference=face_recognition.face_distance(encoded_imgs_output,Encoded_Face)#calculates the difference(similarity) between the face in the frame and the list of encoded faces
        p=face_difference
        #print(face_difference)#prints a list of decimal values for each element telling you how similar the captured face in the frame is to each image stored in the images file
        #the lower the value of the decimal the less the difference between the face in the video and the faces in the images folder
        ########################################################################################################################################
        # Finding the index of the minimum value in the list
        min_value = face_difference[0]#setting the first element of the list the minimum value so there's something to compare the next element to
        match_index = 0#seeting the index to 0 as the min value
        for i in range(len(face_difference)):#iterates through the elements of the list face_difference
            if face_difference[i] < min_value:#if the elements value is less than the minimum value of some element stored...
                min_value = face_difference[i]#the minimum value is the value of the current element
                match_index = i#the element with the minimum value in the array has its index stored within the variable match_index
            #print("Index of smallest value", match_index)
        ########################################################################################################################################
        if match_found[match_index] == True:
            print(Ids[match_index])
        print(match_found)
        print(match_index)






########################################################################################################################################
    cv2.imshow("Face_Attendance_system", Backgroundimg)#displays the background img every frame
    cv2.waitKey(1) # introduce a delay between each displayed frame in OpenCV. with a 1ms dealy
    if cv2.waitKey(1) & 0xFF == ord("q"):#if a key is pressed and it has the ASCII value 'q' the program breaks
        break 