import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("download.jpg")
img_Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_Gray, 1.1, 4)

for (x,y,w,h)  in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("image",img)


cv2.waitKey()
cv2.destroyAllWindows()
