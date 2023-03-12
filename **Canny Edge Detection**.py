import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# def nothing(x):
#     pass


# cv.namedWindow('Trackbars')

# cv.createTrackbar('Threshold1', 'Trackbars', 0, 500, nothing)
# cv.createTrackbar('Threshold2', 'Trackbars', 0, 500, nothing)

# while True:

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/messi5.jpg', 0)

# pos1 = cv.getTrackbarPos('Threshold1', 'Trackbars')
# pos2 = cv.getTrackbarPos('Threshold2', 'Trackbars')

canny = cv.Canny(img, 100, 200)

# cv.imshow('Image', img)
# cv.imshow('Canny', canny)

titles = ['Image', 'Canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Add Trackbar
