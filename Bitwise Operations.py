import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('/Images/final.png')

# bitAnd = cv2.bitwise_and(img2, img1)
# bitOr = cv2.bitwise_or(img2, img1)
# bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
# cv2.imshow('Final', bitAnd)
# cv2.imshow('Final', bitOr)
# cv2.imshow('Final', bitXor)
cv2.imshow('Final1', bitNot1)
cv2.imshow('Final2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
