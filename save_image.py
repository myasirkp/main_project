import numpy as np
import cv2
img =cv2.imread('/home/pi/Desktop/image.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord ('s'):
    cv2.imwrite('/home/pi/Desktop/test_lib/image.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
