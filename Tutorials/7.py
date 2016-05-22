import numpy as np
import cv2

img = cv2.imread('messi.jpg')
# [:2], get 2 first value in shape array
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)


# newmask is the mask image I manually labelled
newmask = cv2.imread('messi_mask.jpg',0)

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]


cv2.imshow('pic', img)

k = cv2.waitKey(0) & 0xFF
if k == 27:   # if press ESC, exit
  cv2.destroyAllWindows()
elif k == ord('s'): # if press 's', Save picture in gray color and exit
  cv2.imwrite('7.png', img)
  cv2.destroyAllWindows()

# plt.imshow(img),plt.colorbar(),plt.show()