import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread("C:/Users/Turing/Downloads/121.jpg",cv.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)

dilation=cv.dilate(mask,kernal,iterations=2)
erosion=cv.erode(mask,kernal,iterations=1)

opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
mg=cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernal)

titles=["Original","Mask","Dilation",
        "Erosion","opening","closing","gradient"]
images=[img,mask,dilation,erosion,opening]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
