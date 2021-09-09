"""
In Smoothening we use High pass filter for edge detection and
Low pass filter for smoothening the image

Gaussian weight covered in this -> Pixels located on the edge
has lower weight and in the middle has higher weight

Gaussian Blur is used to remove the high frequency noise present
in the image

Median Filter is used when we have salt and pepper noise
it replaces the filters with the median of the neighbouring filters

In Bilateral Filter the borders of the image is preserved
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread("C:/Users/Turing/Pictures/Siddhu+2.jpg")

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/25
dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))
#parameters in bilateral filter (img,diameter of each pixel
# neighbourhood, sigmacolor is the filter sigma is color space,
# and the sigma distance is the filter sigma is co-ordinate space
bilateral=cv.bilateralFilter(img,9,75,75)

gblur=cv.GaussianBlur(img,(5,5),0)

# Kernal size must be odd and also greater than 1
median=cv.medianBlur(img,5)
titles=["Original","2D-Convolution","Blur","Gaussian Blur","Median","Bi-lateral"]
images=[img,dst,blur,gblur,median,bilateral]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.xticks([]),plt.yticks([])
    plt.title(titles[i])
plt.show()
cv.destroyAllWindows()