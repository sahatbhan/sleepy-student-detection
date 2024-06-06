import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import time


mixer.init()
sound = mixer.Sound('alarm.wav')

face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')



lbl=['Close','Open']

model = load_model('models/cnncat2.h5')
path = os.getcwd()
cap = cv2.VideoCapture(0)                                               #input from FE
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
i=0
count=0
score=0
state=0
thicc=2
rpred=[99]
lpred=[99]

while(True):
    ret, frame = cap.read()
    height,width = frame.shape[:2] 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
    left_eye = leye.detectMultiScale(gray)
    right_eye =  reye.detectMultiScale(gray)
    
    face_count = 0 # edit it to 1 if you want the number to start with 1
    for(ex, ey, ew, eh) in faces:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
        cv2.putText(frame, 'Face #' + str(face_count), (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        # print(faces)
        # print('------------')
        # print(faces.shape)
        face_count += 1
        for (x,y,w,h) in right_eye:
            r_eye=frame[y:y+h,x:x+w]
            count=count+1
            r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
            r_eye = cv2.resize(r_eye,(24,24))
            r_eye= r_eye/255
            r_eye=  r_eye.reshape(24,24,-1)
            r_eye = np.expand_dims(r_eye,axis=0)
            # rpred = model.predict_classes(r_eye)
            rpred = np.argmax(model.predict(r_eye), axis=-1)            #updated this line. upar wali line is outdated
            if(rpred[0]==1):
                lbl='Open' 
            if(rpred[0]==0):
                lbl='Closed'
            break
        for (x,y,w,h) in left_eye:
            l_eye=frame[y:y+h,x:x+w]
            count=count+1
            l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
            l_eye = cv2.resize(l_eye,(24,24))
            l_eye= l_eye/255
            l_eye=l_eye.reshape(24,24,-1)
            l_eye = np.expand_dims(l_eye,axis=0)
            #lpred = model.predict_classes(l_eye)
            lpred = np.argmax(model.predict(l_eye), axis=-1)            #updated this line. upar wali line is outdated
            if(lpred[0]==1):
                lbl='Open'   
            if(lpred[0]==0):
                lbl='Closed'
            break
        if(rpred[0]==0 and lpred[0]==0):
            score=score+1
        # if(rpred[0]==1 or lpred[0]==1):
        else:
            score=score-1
        if(score<0):    
            score=0
        cv2.putText(frame,'Score:'+str(score),(ex,ey-20), font, 1,(255,255,255),1,cv2.LINE_AA)
        

    # cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

    # for (x,y,w,h) in faces:
    #     cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )

    # for (x,y,w,h) in right_eye:
    #     r_eye=frame[y:y+h,x:x+w]
    #     count=count+1
    #     r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
    #     r_eye = cv2.resize(r_eye,(24,24))
    #     r_eye= r_eye/255
    #     r_eye=  r_eye.reshape(24,24,-1)
    #     r_eye = np.expand_dims(r_eye,axis=0)
    #     # rpred = model.predict_classes(r_eye)
    #     rpred = np.argmax(model.predict(r_eye), axis=-1)            #updated this line. upar wali line is outdated
    #     if(rpred[0]==1):
    #         lbl='Open' 
    #     if(rpred[0]==0):
    #         lbl='Closed'
    #     break

    # for (x,y,w,h) in left_eye:
    #     l_eye=frame[y:y+h,x:x+w]
    #     count=count+1
    #     l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
    #     l_eye = cv2.resize(l_eye,(24,24))
    #     l_eye= l_eye/255
    #     l_eye=l_eye.reshape(24,24,-1)
    #     l_eye = np.expand_dims(l_eye,axis=0)
    #     #lpred = model.predict_classes(l_eye)
    #     lpred = np.argmax(model.predict(l_eye), axis=-1)            #updated this line. upar wali line is outdated
    #     if(lpred[0]==1):
    #         lbl='Open'   
    #     if(lpred[0]==0):
    #         lbl='Closed'
    #     break

    # if(rpred[0]==0 and lpred[0]==0):
    #     score=score+1
    # # if(rpred[0]==1 or lpred[0]==1):
    # else:
    #     score=score-1
    # i=0   
    # if(score<0):
    #     score=0   
    # cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    if(score>15):
        #person is feeling sleepy so we beep the alarm
        cv2.imwrite(os.path.join(path,'image.jpg'),frame)
        
        while(i<1):
            state+=1
            i=1
        try:
            sound.play()
        except:
            pass                                                                        # isplaying = False
        if(thicc<16):
            thicc= thicc+2
        else:
            thicc=thicc-2
            if(thicc<2):
                thicc=2
        cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(state)
print(face_count)
cap.release()
cv2.destroyAllWindows()
