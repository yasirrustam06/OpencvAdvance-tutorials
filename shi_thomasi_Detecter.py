import cv2
import numpy as np

img=cv2.imread("block3.png")
img = cv2.resize(img,(1000,650))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.05, 50)

# convert corners values to integer
# So that we will be able to draw circles on them
corners = np.int0(corners)

for i in (corners):
    x,y=i.ravel()
    cv2.circle(img,(x,y),10,(255,0,255),-1)
    cv2.imwrite("ShiCorner_Image.png",img)
    cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



