import cv2 as cv

import numpy as np

img=cv.imread("C:/Users/Turing/Downloads/smartie.jpg")
imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

l_r=np.array([104,7,0])
h_r=np.array([158,255,255])

fr=cv.inRange(imghsv,l_r,h_r)
im=cv.bitwise_and(img,img,mask=fr)


kernal=np.ones((3,3),np.uint8)
erosion=cv.erode(fr,kernal,iterations=4)
#cv.imshow("erode",erosion)
#cv.imshow("Mask",fr)
dilation=cv.dilate(erosion,kernal,iterations=3)

final=cv.bitwise_and(img,img,mask=dilation)

#cv.imshow("Fina",dilation)
#cv.imshow("Fin",final)
contours=cv.findContours(dilation,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[-2]
C_max=max(contours,key=cv.contourArea)
(x,y,w,h)=cv.boundingRect(C_max)

cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("Image",img)
"""

cv.imshow("Final",im)
cv.imshow("Image",img)

"""

cv.waitKey(0)
cv.destroyAllWindows()
"""
cap=cv.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    frhsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_r=np.array([29,86,6])
    h_r=np.array([100,255,255])
    mask=cv.inRange(frhsv,l_r,h_r)
    #contor=cv.findContours(mask.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv.destroyAllWindows()
"""