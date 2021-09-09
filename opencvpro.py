import numpy as np
import cv2 as cv
"""
def click_event(event,x,y,flags,params):
    if(event==cv.EVENT_LBUTTONDOWN):
        blue  =  img[y,x,0]
        green =  img[y,x,1]
        red   =  img[y,x,2]
        text=str(blue)+" , "+str(green)+" , "+str(red)
        print(text)
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,text,(x,y),font,1,(12,255,255),2)
        cv.imshow("image",img)
        cv.waitKey(0)


img=cv.imread("C:/Users/Turing/Downloads/eew.jfif")
cv.imshow("image",img)
cv.setMouseCallback("image",click_event)
cv.waitKey(0)
cv.destroyAllWindows()

"""
while(True):
    frame=cv.imread("C:/Users/Turing/Downloads/eew.jfif")

    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_b = np.array([ 200, 120, 0])

    u_b = np.array([250, 160, 20])

    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("frame",frame)
    cv.imshow("mas",mask)
    cv.imshow("fnew",res)
    key=cv.waitKey(1)
    if key==27:
        break

cv.destroyAllWindows()