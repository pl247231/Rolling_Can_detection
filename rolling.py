
import cv2 as cv
import numpy as np

cap = cv.VideoCapture('original.MOV')
detected = 0
total = 0
frame1 = 1
copy1 = 1

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('detected.MOV', cv.VideoWriter_fourcc('m','p','4','v'), 60, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    copy = frame.copy()
    total += 1
    blurred = cv.blur(frame, (3,2))
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 1000, param1=70, param2=25, minRadius=14, maxRadius=19)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        param = circles[0][0]     
        cv.circle(frame, (param[0], param[1]), param[2], (0, 255, 0), 2)
        cv.circle(frame, (param[0], param[1]), 2, (0, 255, 0), 3)
        detected += 1

    cv.putText(frame, "Percentage:" + str(int(round(detected/total, 2)*100)) + "%", (330, 70), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv.LINE_AA)
    cv.putText(frame, "Frames With Circles:" + str(detected), (20, 70), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv.LINE_AA)
    cv.putText(frame, "Frame:" + str(total), (230, 70), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv.LINE_AA)
    out.write(frame)
    cv.imshow('video', np.hstack([frame, copy]))
    frame1 = frame
    copy1 = copy
    if cv.waitKey(5) == ord(' '):
        break
cv.imshow('video', np.hstack([frame1, copy1]))
cv.waitKey(0)

print("Frames: " + str(total))
print("Frames with circles: " + str(detected))
print("Percentage: " + str(int(round(detected/total, 2)*100)) + "%")

cap.release()
cv.destroyAllWindows()
