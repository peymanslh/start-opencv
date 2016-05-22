import cv2
import numpy as np

img = cv2.imread('pixel.jpg')

# Show color of pixel 100-100
px = img[55, 99]
print "px", px

# Show blue color of pixel 100-100
cblue = img[30, 40, 0]
print cblue

# Change color of pixel 100-100
img[30, 40] = [255, 255, 255]
print "print img 100, 100", img[30, 40]

# Show image properties
print "number of rows, columns and channels: ", img.shape
print "Image size: ", img.size
print "Image datatype is: ", img.dtype

# draw blue border on img
BLUE = [255,0,0]
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

cv2.imshow('blue border', constant)

k = cv2.waitKey(0) & 0xFF
if k == 27:		# if press ESC, exit
	cv2.destroyAllWindows()
elif k == ord('s'):	# if press 's', Save picture in gray color and exit
	cv2.imwrite('3.png', constant)
	cv2.destroyAllWindows()
