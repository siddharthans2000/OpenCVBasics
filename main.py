
import cv2

import numpy as np

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10 ,(0,255,0),-1)
        points.append((x,y))
        if(len(points)>=2):
            cv2.line(img,points[-1],points[-2],(0,255,0),thickness=2)
        cv2.imshow("Clicked",img)

img=np.zeros((500,500,3),np.uint8)
cv2.imshow("Clicked",img)
points=[]
cv2.setMouseCallback("Clicked",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
