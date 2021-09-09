import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread("C:/Users/Turing/Downloads/dog.jpg")
cv.imshow("image",img)
plt.imshow(img)
# TO remove the marking in matlabplt we have to use
plt.xticks([]),plt.yticks([])
plt.show()
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()