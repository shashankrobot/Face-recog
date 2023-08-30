import os 
import cv2
import face_recognition
import pickle
########################################################################################################################################
img_names_list=[]#stores a list of the images IDs alongside the .PNG
Ids=[]#stores the ID part of the images names
path = "Images"#path to access the images folder
dir_list = os.listdir(path)## Retrieve a list of all png's (files and directories) present in the specified directory path
for i in dir_list:#copies the full image name from all images in the dirlist list into a permanant area to store named img_names_list 
    img_names_list.append(i)
for i in img_names_list:#iterates thorugh the img_names_list
    a,b = i.split('.', 1)# for every element of the img_names_list the element is split into 2 where there is a . in order to remove the png
    Ids.append(a)
#print(Ids)
########################################################################################################################################
#Creating a list with pixel data of all images located in the Image File
Img_List=[]#creates a list of all the images read by cv2 in a foldeer
Image_Folder_Path='Images'#used in for loop to extract images and read them from a specific directory
Images_Names_List=os.listdir(Image_Folder_Path)#stores a list of all the png names
for path in Images_Names_List:#get the directory(file location) of the images and read the images and store this pxiel dat in a list
    Img_List.append(cv2.imread((str(Image_Folder_Path+'/'+path))))
#print(Img_List)
########################################################################################################################################
#encoding all the images
def encoder(Img_List):
    encoded_imgs = []
    for img in Img_List:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#converts the colour of image read using cv2 library from BGR to RGB
        encode = face_recognition.face_encodings(img)[0]#the function takes an image as input and returns a list of face encoding found in the image
        #since we are only interest in 1 face we use index 0 to access only the first faces encoding values generated
        encoded_imgs.append(encode)#appending the encoded values for the image to a specific list
    return encoded_imgs#reutrning the list with all the encoded images values

print('encoding commencing.....')
encoded_imgs_output = encoder(Img_List)#creating a list which is the output of the function to store the list permanantly and later access
print('encoding completed')
#print(encode_imgs_output)
########################################################################################################################################
#storing the encode_imgs_output array alongside the Ids list
encoded_imgs_with_IDs = [encoded_imgs_output,Ids]# Creating a list containing the encoded images output and their corresponding IDs
file = open("EncodedData.p", "wb")# Open a file named "EncodedData.p" in binary write mode ("wb")
pickle.dump(encoded_imgs_with_IDs, file)# Serialize and dump the encoded_imgs_with_IDs list into the file using pickle
file.close()# Closes the file after writing



