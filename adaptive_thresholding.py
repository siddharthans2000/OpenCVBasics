"""
Simple Thresholding may not be usefull for cases whre the lighting
differs from point to point we are using adaptive thresholding

Adaptive filtering uses thresholding in different regions of
the image.

"""

import cv2 as cv

#img=cv.imread("C:/Users/Turing/Downloads/dog.jpg",0)
cap=cv.VideoCapture(0)
while(True):
    _,frame=cap.read()
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame=cv.resize(frame,(512,512))
    cv.imshow("Image", frame)
    th1=cv.adaptiveThreshold(frame,255,cv.ADAPTIVE_THRESH_MEAN_C,
                         cv.THRESH_BINARY,11,2)
    th2=cv.adaptiveThreshold(frame,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv.THRESH_BINARY_INV,11,2)
    cv.imshow("th1",th1)
    cv.imshow("th2",th2)
    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv.destroyAllWindows()