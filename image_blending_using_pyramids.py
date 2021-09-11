"""
To blend 2 images, we use python to make that possible
To blend 2 images we blend them in each laplacian pyramids
"""
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
apple=cv.imread("C:/Users/Turing/Downloads/apple.jpg")
apple=cv.resize(apple,(512,512))
orange=cv.imread("C:/Users/Turing/Downloads/orange.jfif")
orange=cv.resize(orange,(512,512))

layer=apple.copy()
gp_apple=[layer]
for i in range(6):
    new_up=cv.pyrDown(layer)
    gp_apple.append(new_up)

layer=orange.copy()
gp_orange=[layer]
for i in range(6):
    new_up=cv.pyrDown(layer)
    gp_orange.append(new_up)

apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    gaussian_extend=cv.pyrUp(gp_apple[i])
    laplace=cv.subtract(gp_apple[i-1],gaussian_extend)
    lp_apple.append(laplace)

orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    gaussian_extend=cv.pyrUp(gp_orange[i])
    laplace=cv.subtract(gp_orange[i-1],gaussian_extend)
    lp_orange.append(laplace)

apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch=apple_lap.shape
    laplace=np.hstack(apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):])
    apple_orange_pyramid.append(laplace)

apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv.add()





