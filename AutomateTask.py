# This file automates taking a picture. Normally, to take a picture, you would have to manually set up the camera, and you can't do it on a computer. 
# But this code takes a picture and uploads it. 

import cv2
import dropbox
import time
import random

start_time = time.time()

def takingPicture():
    number = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):

        ret,frame = videoCaptureObject.read()
       
        img_name = "img"+str(number)+".jpeg"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
   
    videoCaptureObject.release()
    cv2.destroyAllWindows()



def uploadPicture(img_name):
    access_token = "RFZYSy94DW4AAAAAAAAAAbEYVGb6sOYMcpmeMOUDjs2xKg0soMmUjKuQERu7WP4Z"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = takingPicture()
            uploadPicture(name)

main()
