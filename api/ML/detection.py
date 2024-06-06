import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import json


def live_cam():
    mixer.init()
    sound = mixer.Sound('sound.wav')

    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    leye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
    reye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')

    model = load_model('cnnCat2.h5')
    path = os.getcwd()
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    i=0
    count=0
    score=0
    state=0
    thicc=2
    rpred=[99]
    lpred=[99]
    all_faces=[]
    all_drowsy=[]

    while(True):
        _, frame = cap.read()
        height,width = frame.shape[:2] 

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
        left_eye = leye.detectMultiScale(gray)
        right_eye =  reye.detectMultiScale(gray)
        
        face_count = 0
        for(ex, ey, ew, eh) in faces:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
            cv2.putText(frame, 'Face #' + str(face_count), (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
            face_count += 1
            for (x,y,w,h) in right_eye:
                r_eye=frame[y:y+h,x:x+w]
                count=count+1
                r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye,(24,24))
                r_eye= r_eye/255
                r_eye=  r_eye.reshape(24,24,-1)
                r_eye = np.expand_dims(r_eye,axis=0)
                rpred = np.argmax(model.predict(r_eye), axis=-1)
                break

            for (x,y,w,h) in left_eye:
                l_eye=frame[y:y+h,x:x+w]
                count=count+1
                l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                l_eye = cv2.resize(l_eye,(24,24))
                l_eye= l_eye/255
                l_eye=l_eye.reshape(24,24,-1)
                l_eye = np.expand_dims(l_eye,axis=0)
                lpred = np.argmax(model.predict(l_eye), axis=-1)
                break
            if(rpred[0]==0 and lpred[0]==0):
                score=score+1
            else:
                score=score-1
            if(score<0):    
                score=0
            cv2.putText(frame,'Score:'+str(score),(ex,ey-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            
        if(score>15):
            while(i<1):
                state+=1
                i=1
            try:
                sound.play()
            except:
                pass
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

    all_faces.append(face_count)
    all_drowsy.append(state)
    cap.release()
    cv2.destroyAllWindows()
    return state, face_count

def video(vid):
    mixer.init()
    sound = mixer.Sound('sound.wav')

    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    leye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
    reye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')

    model = load_model('cnnCat2.h5')
    path = os.getcwd()
    cap = cv2.VideoCapture(vid)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    i=0
    count=0
    score=0
    state=0
    thicc=2
    rpred=[99]
    lpred=[99]
    all_faces=[]
    all_drowsy=[]

    while(True):
        _, frame = cap.read()
        height,width = frame.shape[:2] 

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
        left_eye = leye.detectMultiScale(gray)
        right_eye =  reye.detectMultiScale(gray)
        
        face_count = 0
        for(ex, ey, ew, eh) in faces:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
            cv2.putText(frame, 'Face #' + str(face_count), (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
            face_count += 1
            for (x,y,w,h) in right_eye:
                r_eye=frame[y:y+h,x:x+w]
                count=count+1
                r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye,(24,24))
                r_eye= r_eye/255
                r_eye=  r_eye.reshape(24,24,-1)
                r_eye = np.expand_dims(r_eye,axis=0)
                rpred = np.argmax(model.predict(r_eye), axis=-1)
                break

            for (x,y,w,h) in left_eye:
                l_eye=frame[y:y+h,x:x+w]
                count=count+1
                l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                l_eye = cv2.resize(l_eye,(24,24))
                l_eye= l_eye/255
                l_eye=l_eye.reshape(24,24,-1)
                l_eye = np.expand_dims(l_eye,axis=0)
                lpred = np.argmax(model.predict(l_eye), axis=-1)
                break
            if(rpred[0]==0 and lpred[0]==0):
                score=score+1
            else:
                score=score-1
            if(score<0):    
                score=0
            cv2.putText(frame,'Score:'+str(score),(ex,ey-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            
        if(score>15):
            while(i<1):
                state+=1
                i=1
            try:
                sound.play()
            except:
                pass
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

    all_faces.append(face_count)
    all_drowsy.append(state)
    cap.release()
    cv2.destroyAllWindows()
    return state, face_count