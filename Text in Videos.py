# Date and Time
# Width and Height

import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # cap.set(3, 640)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # cap.set(4, 480)

# cap.set(3, 1280)  # Camera adjusts to it's Resolution
# cap.set(4, 720)  # Camera adjusts to it's Resolution

# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_PLAIN
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 3, (255, 255, 255), 3, cv2.LINE_AA)
        frame = cv2.putText(frame, datet, (500, 100), font, 3, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()