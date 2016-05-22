# Image Processing in OpenCV > Template Matching
import cv2
import numpy as np

img = cv2.imread('messi.jpg',0)
img2 = img.copy()
template = cv2.imread('messi_face.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
  'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
  img = img2.copy()
  method = eval(meth)

  # Apply template Matching
  res = cv2.matchTemplate(img,template,method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
  else:
    top_left = max_loc
  bottom_right = (top_left[0] + w, top_left[1] + h)

  cv2.rectangle(img,top_left, bottom_right, 255, 2)

  cv2.imshow('result', res)
  cv2.imshow('img', img)

k = cv2.waitKey(0) & 0xFF
if k == 27:   # if press ESC, exit
  cv2.destroyAllWindows()
elif k == ord('s'): # if press 's', Save picture in gray color and exit
  cv2.imwrite('6.png', res)
  cv2.destroyAllWindows()
