import cv2 as cv
import numpy as np
import time
cap=cv.VideoCapture(0)
time.sleep(2)
while(cap.isOpened()):

    _,frame=cap.read()
    img2hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_r=np.array([163,87,170])
    h_r=np.array([255,255,255])
    fi=cv.inRange(img2hsv,l_r,h_r)
    kernel=np.ones((2,2),dtype=np.uint8)
    erosion=cv.erode(fi,kernel,iterations=2)
    dilate=cv.dilate(erosion,kernel,iterations=2)
    contours=cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[-2]
    if(len(contours)>0):
        C_max=max(contours,key=cv.contourArea)

        (x,y,w,h)=cv.boundingRect(C_max)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.imshow("Frame",frame)
    if(cv.waitKey(40) & 0xFF==ord('q')):
        break

cap.release()
cv.destroyAllWindows()