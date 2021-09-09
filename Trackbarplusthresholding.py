import cv2 as cv
import numpy as np
def nothing(x):
    pass
cv.namedWindow("Tracking")
cap=cv.VideoCapture(0)
cv.createTrackbar("LH","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)
cv.createTrackbar("HH","Tracking",255,255,nothing)
cv.createTrackbar("HS","Tracking",255,255,nothing)
cv.createTrackbar("HV","Tracking",255,255,nothing)

while True:
    ret,frame=cap.read()
    frame=cv.resize(frame,(512,512))
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_h=cv.getTrackbarPos("LH","Tracking")
    l_s = cv.getTrackbarPos("LS", "Tracking")
    l_v = cv.getTrackbarPos("LV", "Tracking")
    h_h = cv.getTrackbarPos("HH", "Tracking")
    h_s = cv.getTrackbarPos("HS", "Tracking")
    h_v = cv.getTrackbarPos("HV","Tracking")

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([h_h,h_s,h_v])

    mask=cv.inRange(hsv,l_b,u_b)

    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("Image",frame)
    cv.imshow("Mask",mask)
    cv.imshow("final",res)
    k=cv.waitKey(1)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()
