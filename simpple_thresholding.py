import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("C:/Users/Turing/Downloads/dasa.jpg")
#For THRESH_BINARY less than threshold is 0 greater than it will be 1
_,th1=cv.threshold(img,150,255,cv.THRESH_BINARY)
#For THRESH_BINARY_INV opposite of THRESH_BINARY
_,th2=cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
#For THRESH_TRUNC less than threshols will as it is but greater then
# threshold will have the same threshold value
_,th3=cv.threshold(img,150,255,cv.THRESH_TRUNC)
#For THRESH_TOZERO, less than threshold will be zeros and greater than
#torezo will be same as it is.(Like Relu Function)
_,th4=cv.threshold(img,150,255,cv.THRESH_TOZERO)

titles=["Original","Threshold Binary","BINARY INVERSE",
       "THRESHOLD TRUNC","THRESHOLD TOZERO"]
images=[img,th1,th2,th3,th4]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()