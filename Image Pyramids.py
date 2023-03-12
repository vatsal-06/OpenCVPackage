import cv2 as cv
import numpy as np

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/lena.jpg')
layer = img.copy()
gp = [layer]

# for i in range(5):
#     layer = cv.pyrDown(layer)
#     gp.append(layer)
#     cv.imshow(str(i), layer)

# for i in range(5):
#     layer = cv.pyrUp(layer)
#     gp.append(layer)
#     cv.imshow(str(i), layer)

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

layer = gp[5]
cv.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussianExtended)
    cv.imshow(str(i), laplacian)

# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)

# hr1 = cv.pyrUp(img)
# hr2 = cv.pyrUp(hr1)
# hr3 = cv.pyrUp(lr2)

# cv.imshow('Pyr.Down.1', lr1)
# cv.imshow('Pyr.Down.2', lr2)

# cv.imshow('Pyr.Up.1', hr1)
# cv.imshow('Pyr.Up.2', hr2)
# cv.imshow('Pyr.Up.3', lr2)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
