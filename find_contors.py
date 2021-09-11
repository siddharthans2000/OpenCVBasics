"""
Find and determine the contours in an image

"""
import numpy as np
import cv2 as cv
def nothing(x):
    pass
img=cv.imread("C:/Users/Turing/Downloads/OpenCV.png")
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow("Threshold")
cv.createTrackbar("T1","Threshold",10,255,nothing)
while(True):
    b=cv.getTrackbarPos("T1","Threshold")
    ret,thresh=cv.threshold(img_gray,b,255,0)
    cv.imshow("threshold",thresh)
    contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    #print("Number of Contours ="+str(len(contours)))
# parameters for drawcontours(source image,contours,
# contours index(-1 to make all)
    #cv.drawContours(img,contours,-1,(0,255,0),3)
    cv.imshow("Image",img)
    cv.imshow("Image Gray",img_gray)
    if(cv.waitKey(1) & 0xFF ==ord('q')):
        break
print(len(contours))
cv.destroyAllWindows()
