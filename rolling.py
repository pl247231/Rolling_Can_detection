import cv2 as cv
import numpy as np

cap = cv.VideoCapture('IMG_4616.MOV')
detected = 0
total = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    copy = frame.copy()
    total += 1
    blurred = cv.medianBlur(frame, 5)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 1000, param1=70, param2=27, minRadius=14, maxRadius=20)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        param = circles[0][0]
        cv.circle(frame, (param[0], param[1]), param[2], (0, 255, 0), 2)
        cv.circle(frame, (param[0], param[1]), 2, (0, 255, 0), 3)
        detected += 1

    cv.putText(copy, "Percentage: " + str(int(round(detected/total, 2)*100)) + "%", (150, 70), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv.LINE_AA)
    cv.imshow('video', np.hstack([frame, copy]))

    if cv.waitKey(5) == ord(' '):
        break

print("Frames: " + str(total))
print("Frames with circles: " + str(detected))
print("Percentage: " + str(int(round(detected/total, 2)*100)) + "%")

cap.release()
cv.destroyAllWindows()
