import cv2 as cv
import numpy as np

img=cv.imread("C:/Users/Turing/Downloads/shap.png")

output=img.copy()
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)
cir=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=0,maxRadius=0)
detected=np.uint16(np.around(cir))
for (x,y,r) in detected[0,:]:
    cv.circle(output,(x,y),r,(0,255,0),2)
    cv.circle(output,(x,y),2,(0,0,255),2)

cv.imshow("Image",output)
cv.waitKey(0)
cv.destroyAllWindows()