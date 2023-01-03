import cv2
import numpy as np

print(cv2.__version__)
image = cv2.imread('./image/face2.jpeg',cv2.IMREAD_UNCHANGED)
height, width, channel = image.shape()
print(height)
print(width)
print(channel)
#변환
image_flip = cv2.flip(image,0)
image_flip = cv2.flip(image,1)
#회전
image_rotate = cv2.getRotationMatrix2D(width/2, height/2,30,1)
cv2.imshow('imagewindow1',image)
cv2.imshow('imagewindow2', image_rotate)
cv2.waitKey(0)
cv2.destroyWindow()
