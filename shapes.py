import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)  # black image

# cv2.polylines()......for polygons
# cv2.ellipse()......for eliptical

img = cv2.line(img, (0, 0), (255, 255), (255, 255, 255), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 255, 255), 5)

img = cv2.rectangle(img, (384, 0), (510, 128), (255, 255, 255), 5)  # -1  will fill shape
img = cv2.circle(img, (447, 63), 63, (255, 255, 255), -1)

font = cv2.FONT_HERSHEY_COMPLEX  # can choose any font by cv2.FONT.... and choose
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
