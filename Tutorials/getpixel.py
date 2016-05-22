import cv2
import numpy as np

# select output file for write list
myFile = open('output.txt', 'w')
# import image
img = cv2.imread('pixel.jpg')
# Get height & width
h, w = img.shape[:2]

imgSize = img.size / 3
myList = range(imgSize)

# Add pixels to a list
ih = 0
iw = 0
for i in range(imgSize):
    if(iw == w-1):
        iw = 0
        ih = ih + 1
        if(ih == h-1):
            ih = 0
    myList[i] = img[ih, iw]
    print ih, iw, i, myList[i]
    iw = iw + 1

# Create new black image
img2 = np.zeros((h,w,3), np.uint8)

# Reverse list
myList.reverse()

# add pixels to new black image
jh = 0
jw = 0
for j in range(imgSize):
    if(jw == w-1):
        jw = 0
        jh = jh + 1
        if(jh == h-1):
            jh = 0
    img2[jh, jw] = myList[j]
    print jh, jw, j, myList[j]
    jw = jw + 1

# Show new image
cv2.imshow('new pic', img2)
# Write myList to output file
for item in myList:
    myFile.write("%s\n" % item)

# Close window
k = cv2.waitKey(0) & 0xFF
if k == 27:		# if press ESC, exit
	cv2.destroyAllWindows()
elif k == ord('s'):	# if press 's', Save picture in gray color and exit
	cv2.imwrite('new-picture.png', img2)
	cv2.destroyAllWindows()
