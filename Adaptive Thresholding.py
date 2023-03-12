import cv2 as cv
import numpy as np

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/sudoku.png', 0)
# _, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Image', img)
# cv.imshow('Threshold', th1)
# cv.imshow('Threshold', th2)
cv.imshow('Threshold', th3)

cv.waitKey(0)
cv.destroyAllWindows()