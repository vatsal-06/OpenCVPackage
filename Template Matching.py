import cv2
import numpy as np

img = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/messi_face.jpg', 0)

w, h = face.shape[::-1]

res = cv2.matchTemplate(gray, face, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
