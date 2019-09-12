import numpy as np
import cv2

cap = cv2.VideoCapture('raw_video_feed.mp4')

# 225 is my bottom row
botrow = 225

while(cap.isOpened()):
    ret, frame = cap.read()
    ret, bnw_frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    width = int(cap.get(3))
    # height = cap.get(4)

    leftwhitespace = 0
    linespace = 0
    ontheleft = True
    ontheright = False
    
    for i in range(width):
        if bnw_frame[ botrow , i , 0 ] == 255 and ontheleft == True:
            leftwhitespace = leftwhitespace + 1
        if bnw_frame[ botrow , i , 0 ] == 0:
            linespace = linespace + 1
            ontheright = True
            ontheleft = False

    print(leftwhitespace)

    center = leftwhitespace + linespace/2

    # circle , frame , position , radius , color , thickness (-1 is solid) 
    cv2.circle(frame, (center, 225), 23, (0, 0, 255), -1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()