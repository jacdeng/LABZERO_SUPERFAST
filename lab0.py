import numpy as np
import cv2

cap = cv2.VideoCapture('raw_video_feed.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.circle(frame, (160, 235), 20, (255, 0, 0), -1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()