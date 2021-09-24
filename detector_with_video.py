import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def region_of_interest(img,vertices):
    mask=np.zeros_like(img) # mask for the size of the image
    #channel_count=img.shape[2] # size of the various color channels used
    match_mask_color=255 # *channel_count # making sure the mask has the same number of channels
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    im=np.copy(img)
    blank_image=np.zeros((im.shape[0],im.shape[1],3),
                         dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_image,(x1,y1),(x2,y2),(0,0,255),2)
            #drawing lines in hte blank image which
            # has the same size as initial image
    img=cv.addWeighted(img,0.8,blank_image,1,0.0)
    return img


def process(image):
    height=image.shape[0]
    width=image.shape[1]
    region_of_interest_points=[(0,height),
                               (width,height),
                               (width/2,height/2)]
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    canny=cv.Canny(gray_image,100,150)
    cropped_image=region_of_interest(canny,
                np.array([region_of_interest_points],np.int32))
    plt.imshow(cropped_image)
    lines=cv.HoughLinesP(cropped_image,rho=5,
                         theta=np.pi/60,threshold=100,
                         lines=np.array([]),
                         minLineLength=40,
                         maxLineGap=200)

    image_with_lines=draw_lines(image,lines)
    return image_with_lines

cap=cv.VideoCapture("C:/Users/Turing/Downloads/Road - 2859.mp4")

while(cap.isOpened()):
    ret,frame=cap.read();
    frame=cv.resize(frame,(500,500))
    final=process(frame)
    cv.imshow("Prediction",final)
    if(cv.waitKey(60) & 0xFF ==ord('q')):
        break
cap.release()
cv.destroyAllWindows()

