import cv2 as cv
import numpy as np
img=cv.imread("C:/Users/Turing/Downloads/not.jpg")
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,thresh=cv.threshold(img_gray,240,255,cv.THRESH_BINARY)

contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
for contour in contours:
    approx=cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    cv.drawContours(img,[approx],0,(0,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if(len(approx)==3):
        cv.putText(img,"Triangle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    elif(len(approx)==4):
        (_,_,w,h)=cv.boundingRect(approx)
        aspectRatio=float(w)/h
        if(aspectRatio>=0.95 and aspectRatio<=1.05):
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img,"Rectanlge",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    elif(len(approx)==5):
        cv.putText(img,"Pentagon",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    else:
        cv.putText(img,"Circle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
cv.imshow("Image",img)
cv.imshow("Image Gray",img_gray)
cv.imshow("Threshold",thresh)
cv.waitKey(0)
cv.destroyAllWindows()