import cv2 as cv
import numpy as np

apple = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/unnamed.jpg')
orange = cv.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/Unknown-3.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# Generate Gaussian Pyramids

apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(apple_orange)
    gp_orange.append(orange_copy)

# Generate Laplacian Pyramid

apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussianExtended)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussianExtended)
    lp_orange.append(laplacian)

# Join half of Two Images

apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple.lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstruct

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv.imshow('Apple', apple)
cv.imshow('Orange', orange)
cv.imshow('Half', apple_orange)
cv.imshow('Reconstruct', apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()
