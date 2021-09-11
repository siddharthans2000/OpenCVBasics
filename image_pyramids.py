"""
Image Pyramids are used when trying to recognize an object in a
image which has different resolutions
1) Gaussian Pyramids
2) Laplacian pyramids
In this process the images undergoes repeated subsampling and
smoothing

Gaussian Pyramids
PyrDown --> Reduce the resolution of the image(information is lost)
PyrUp ---> Increase the dimension of the image

Laplacian Pyramids
(No exclusive functions for laplacian pyramids used Gaussian
pyramids with some extended functionalities)
laplacian pyramid is the difference between that level in
gaussian pyramid and expanded version of its
upper level in gaussian pyramid.
"""
import cv2 as cv

img=cv.imread("C:/Users/Turing/Downloads/lena.jpg")
layer=img.copy()
gp=[layer]
#Gaussian part
for i in range(6):
    layer=cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i),layer)
#Laplacian part
for i in range(5,0,-1):
    gaussian_extended=cv.pyrUp(gp[i])
    laplacian=cv.subtract(gp[i-1],gaussian_extended)
    cv.imshow(str(i),laplacian)
layer=gp[5]
cv.imshow("Upper Gaussian",layer)
cv.waitKey(0)
cv.destroyAllWindows()