import numpy as np
import cv2

# Show picture in a window
img = cv2.imread('pic.jpg', 0)
cv2.imshow('image', img)

k = cv2.waitKey(0) & 0xFF
if k == 27:		# if press ESC, exit
	cv2.destroyAllWindows()
elif k == ord('s'):	# if press 's', Save picture in gray color and exit
	cv2.imwrite('1.png', img)
	cv2.destroyAllWindows()