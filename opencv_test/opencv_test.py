import cv2
import numpy as np

print(cv2.__version__)
image = cv2.imread('./image/face.jpeg',cv2.IMREAD_UNCHANGED)
print(image.shape)
# cv2.imshow('imagewindow', image)
# cv2.waitKey(0)
# cv2.destroyWindow()
