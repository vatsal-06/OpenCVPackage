import cv2
import numpy as np

img = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/OpenCV_Logo.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Number of Contours = ' + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
# We can give any number from 0-11 (No. of Contours)
# For drawing all use -1

cv2.imshow('Image', img)
# cv2.imshow('Image Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
