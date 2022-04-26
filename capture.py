import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number =random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result =True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()

def uploadFile(img_name):
     #access_token='sl.BGeMIwRy8cIe5YUWGdXrjL6837RscnsGWB8XC3QXM9m2isCWkEBkyvDPY5qLYTOprc_CHyS-GOdkusNP4S-Kx-JNrQqXVPnw9Hmy2WvAmjybHIAtcQNWiyyJuk7KAxoqi0YGC8KvbAY'
     access_token = 'sl.BGek2EK4X1HimaSUQg-1YpAIKRL_Xr2USgA7nWJJn3SYggGCRXpwj_bqsZCfAhNQSFVVGasKtVjpzKKmla2p_i7W8mCYfZ5o2rkEXF5ilsc5wiD8zTl9ApFa7iwMx7sh31BiiaH0D4ot'
     file=img_name
     file_from=file
     file_to="/snaps/"+(img_name)
     dbx=dropbox.Dropbox(access_token)
     with open (file_from,'rb') as f:
         dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
         print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=20):
            name=take_snapshot()
            uploadFile(name)

main()





