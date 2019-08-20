# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:47:21 2018

@author: Shani Singh
"""

import cv2
import numpy as np
face=cv2.CascadeClassifier('C:\\New folder\\Lib\\site-packages\\cv2\\data\\haarscascade_frontalface_default.xml')
print(face)
cam=cv2.VideoCapture(0)
while(True):
    ret,img=cam.read();
    if ret is True:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        pass
    faces=face.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("face",img)
    if(cv2.waitKey(0)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
