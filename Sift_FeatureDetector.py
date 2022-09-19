
import cv2
import cv2 as cv
import numpy as np

# read the image
img=cv.imread("sift1.jpg")
img = cv2.resize(img,(1000,650))


# convert the given image to grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# create the sift detecter
sift=cv.SIFT_create()
# find the keypoint .key points are simply the blobs,corner,edges etc

# kp=sift.detect(img,None)

# to compute the descripter..we can directly compute without finding the keypoints
kp,des=sift.detectAndCompute(img,None)

# draw the keypoints
keypoints=cv.drawKeypoints(gray,kp,img)
# keypoints=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# display the image
cv2.imwrite("SiftDetector_Image.jpeg",img)
cv.imshow("image",img)
cv.waitKey()
cv.destroyAllWindows()




















