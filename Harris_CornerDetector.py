import cv2 as cv
import numpy as np

img=cv.imread("block3.png")
print(img.shape)
img = cv.resize(img,(1000,650))

# Changing into gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=np.float32(gray)

# AppLying The Harris Corner Detector
dst = cv.cornerHarris(gray,2,3,0.04)
dst=cv.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]

cv.imwrite("Harris_CornerDetectedImage.png",img)
cv.imshow("image",img)
cv.waitKey()
cv.destroyAllWindows()

