import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/sudoku.png', cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelx = np.uint8(np.absolute(sobelx))

sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
sobely = np.uint8(np.absolute(sobely))

edges = cv.Canny(img, 100, 200)

sobelCombined = cv.bitwise_or(sobelx, sobely)

titles = ['Image', 'Laplacian', 'Sobel.X', 'Sobel.Y', 'Sobel.Combined', 'Canny']
images = [img, lap, sobelx, sobely, sobelCombined, edges]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
