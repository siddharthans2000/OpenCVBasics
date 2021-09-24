"""
Hough transforms says about converting all hte points form
xy plane to mc plane, as we all know that it is quite easy to
manage one point than a lot of points.

Two kinds of Hough Line Transforms

1) The standard hough transform
2) The probabilistic Hough line transform

"""
def nothing(x):
    pass
import cv2 as cv
import numpy as np
img=cv.imread("C:/Users/Turing/Downloads/sudoku.jpg")
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(img_gray,50,150,apertureSize=3)
lines=cv.HoughLines(edges,rho=1,theta=np.pi / 180,threshold= 200)
for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho

    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow("image",img)
cv.imshow("Canny",edges)
k=cv.waitKey(0)
cv.destroyAllWindows()

"""
cv.namedWindow("Threshold")
cv.createTrackbar("T1","Threshold",0,255,nothing)
cv.createTrackbar("T2","Threshold",0,255,nothing)
while(True):
    a=cv.getTrackbarPos("T1","Threshold")
    b=cv.getTrackbarPos("T2","Threshold")
    can=cv.Canny(img_gray,a,b,apertureSize=3)
    # rho is distance resolution of accumulator in pixels
    # theta is angle resolution of accumulator in radians
    # threshold accumlator threshold parameter
    lines=cv.HoughLines(can,rho=1,theta=np.pi/180,threshold=200)
    for line in lines:
        rho, theta= line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho

        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))

        x2=int(x0-1000*(-b))
        y2=int(y1-1000*(a))

        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    if(cv.waitKey(1) & 0xFF==ord('q')):
        break
    cv.imshow("Image",img)
cv.destroyAllWindows()
"""