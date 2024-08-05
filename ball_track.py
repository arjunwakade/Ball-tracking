import cv2 as cv
import numpy as np
video = cv.VideoCapture('ball.mp4')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower = np.array([25, 50, 70])
    upper = np.array([35, 255, 255])
    frame_mask = cv.inRange(frame_hsv, lower, upper)
    result = cv.bitwise_and(frame, frame, mask = frame_mask)
    contours, hierarchy = cv.findContours(frame_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, width, height = cv.boundingRect(max(contours, key=cv.contourArea))
        cv.circle(frame, (int(x+(width/2)),int(y+(height/2))), int((width+height)/4), (255,255,255),2)
    cv.imshow("Ball Tracking", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()