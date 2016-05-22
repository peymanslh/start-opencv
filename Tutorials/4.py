import cv2
import numpy as np


# Load two images
img1 = cv2.imread('pic.jpg')
img2 = cv2.imread('opencv.jpg')

# simply add img1 on img2
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)

cv2.imshow('new', dst)

k = cv2.waitKey(0) & 0xFF
if k == 27:   # if press ESC, exit
  cv2.destroyAllWindows()
elif k == ord('s'): # if press 's', Save picture in gray color and exit
  cv2.imwrite('4.png', img1)
  cv2.destroyAllWindows()