import cv2
import numpy as np

img = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/chessboard.png')

# cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.08)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('DST', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
