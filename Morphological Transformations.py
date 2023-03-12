import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/smarties.png', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dialation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
# One can apply many other Effects

titles = ['Image', 'Mask', 'Dialation', 'Erosion', 'Opening', 'Closing', 'Gradient']
images = [img, mask, dialation, erosion, opening, closing, mg]

for i in range(7):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
