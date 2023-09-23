import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype ='uint8')
# cv.imshow('Blank', blank)

# # 1. paint the image a cerain color
# # 0, 255, 0 (green)
# # 0 , 0, 255 (red)
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# # 2. draw a rectangle
# # cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness = cv.FILLED) # try thickness = 20, thickness = -1 also means filled
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)
# cv.imshow('Rectanle', blank)

# # 3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1)
# cv.imshow('Circle', blank)

# # 4. draw a line
# cv.line(blank, (blank.shape[1]//4, blank.shape[0]//4), (blank.shape[1]//2, blank.shape[0]//4), (255, 255, 255), thickness = 3)
# cv.imshow('Line', blank)

# 5. write text
cv.putText(blank, 'Hello, my name is Wei-Hsuan', (0, 255), cv.FONT_HERSHEY_TRIPLEX, .5, (0, 255, 0), 1)
cv.imshow('Text', blank)


cv.waitKey(0)