import numpy as np
import cv2

cap = cv2.VideoCapture('raw_video_feed.mp4')

# 225 is bottom row
botrow = 225

while(cap.isOpened()):
    ret, frame = cap.read()
    ret, bnw_frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    width = int(cap.get(3))

    on_line = False

    for i in range(width):
        if bnw_frame[ botrow , i , 0 ] == 0:
            linestart = i
            on_line = True
        if bnw_frame[ botrow , i , 0 ] == 255 and on_line == True:
            linestop = i - 60
            on_line = False

    center = (linestop + linestart) / 2

    # circle , frame , position , radius , color , thickness (-1 is solid) 
    cv2.circle(frame, (center, 225), 23, (0, 0, 255), -1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
