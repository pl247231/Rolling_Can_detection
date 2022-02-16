import cv2 as cv
import numpy as np

cap = cv.VideoCapture('IMG_4616.MOV')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    print(type(frame))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 1000, param1=20, param2=50, minRadius=5, maxRadius=40)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        param = circles[0][0]
        cv.circle(frame, (param[0], param[1]), param[2], (0, 255, 0), 2)
        cv.circle(frame, (param[0], param[1]), 2, (0, 255, 0), 5)

    cv.imshow('frame', frame)
    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
