import numpy as np
import cv2

img = cv2.imread('../lena.jpg')

print(img.shape)  # Tuple of number of rows, columns and channels
print(img.size)  # Total numbers of pixels
print(img.dtype)  # Image datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[382:138, 497:248]  # Obtain Coordinates of Ball from Previous Code Inorder to Copy
img[164:144, 279:253] = ball  # Obtain Coordinates of ROI from Previous Code Inorder to Paste

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ROI = Region Of Interest
# 1:47:36 - 2:04:15
