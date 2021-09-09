"""
An Image gradient is a directionsla change in the intensity or
color in an image
1) Laplacian Methods
2) Sobel X -> Edge Detections along horizontal
3) Sobel Y -> Edge Detection along Vertical
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread("C:/Users/Turing/Downloads/dog.jpg",cv.IMREAD_GRAYSCALE)
# Laplacian parameters (image,data type 64 bit float,kernel size(default available))
#64 bit float it deals with the negative number when using laplacian
# transform
lap=cv.Laplacian(img,cv.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
# for SobelX we need to keep the dx variable to 1 and dy=0
sobelX=cv.Sobel(img,cv.CV_64F,dx=1,dy=0)
# for SobelY we need to keep the dx variable to 0 and dy=1
sobelY=cv.Sobel(img,cv.CV_64F,dx=0,dy=1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

# Combining both SobelX and SobelY using BIT or operator
sobelCombined=cv.bitwise_or(sobelX,sobelY)
titles=["Original","Laplacian","Sobel X","Sobel Y","Sobel_Combined"]
images=[img,lap,sobelX,sobelY,sobelCombined]
for i in range(len(titles)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.xticks([]),plt.yticks([])
    plt.title(titles[i])
plt.show()