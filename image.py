# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:44:13 2018

@author: Shani Singh
"""

import cv2
'''
img=cv2.imread(' ')
img=cv2.imread(' ')
print(img)
imgr=cv2.resize(img,(600,600))
cv2.imshow('open',img)
'''
cap=cv2.VideoCapture(0)
face_recog=cv2.CascadeClassifier('C:\\New folder\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
while(True):
    ret,frame=cap.read()
    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_recog.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Finding faces...",frame)
        if cv2.waitkey(1)==27:
            break
    else:
        print("Camera not available")
        break
cv2.destroyAllWindows()