"""
Canny Edge Detection algorithm uses multi stage algorithm to
detect a wide range of edges in the image
Process in 5 steps
1) Noise reduction using gaussian filter (smoothing)
2) Intensity gradient of the image
3) Apply Non max suppression
4) Double threshold on potential edges
5) Track edges using Hysteresis:-> supression all the edges that are
weak or not connected to strong edges
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img=cv.imread("C:/Users/Turing/Downloads/sudoku.jpg",0)
img=cv.resize(img,(500,500))

cv.namedWindow("Canny")

cv.createTrackbar("Threshold1","Canny",100,255,nothing)
cv.createTrackbar("Threshold2","Canny",200,255,nothing)

while(True):

    thres1=cv.getTrackbarPos("Threshold1","Canny")
    thresh2=cv.getTrackbarPos("Threshold2","Canny")
    canny = cv.Canny(img, thres1, thresh2)
    cv.imshow("Original",img)
    cv.imshow("Canny Image",canny)
    if(cv.waitKey(1) & 0xFF == ord('q')):
        break
cv.destroyAllWindows()