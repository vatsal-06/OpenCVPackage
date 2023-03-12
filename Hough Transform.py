import cv2
import numpy as np

img = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

for line in lines:

    rho, theta = line[0]

    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))  # Round Off Value of (r * cos(theta) - 1000 * sin(theta))
    y1 = int(y0 + 1000 * a)  # Round Off Value of (r * sin(theta) + 1000 * cos(theta))

    x2 = int(x0 - 1000 * (-b))  # Round Off Value of (r * cos(theta) + 1000 * sin(theta))
    y2 = int(y0 - 1000 * a)  # Round Off Value of (r * sin(theta) - 1000 * cos(theta))

    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Image', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
