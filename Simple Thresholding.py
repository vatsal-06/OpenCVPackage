import cv2 as cv

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/gradient.png')
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow('Image', img)
cv.imshow('Threshold1', th1)
cv.imshow('Threshold2', th2)
cv.imshow('Threshold3', th3)
cv.imshow('Threshold4', th4)
cv.imshow('Threshold5', th5)

cv.waitKey(0)
cv.destroyAllWindows()
