import cv2

img = cv2.imread('/Users/vatsalgupta/Desktop/OpenCv/Images/shapes.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, 'Square', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 7:
        cv2.putText(img, 'Septagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 8:
        cv2.putText(img, 'Octagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 9:
        cv2.putText(img, 'Nonagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, 'Decagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))


cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
