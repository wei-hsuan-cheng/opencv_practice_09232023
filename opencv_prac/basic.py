import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Park', gray)

# blur (Gaussian blur)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # the 2nd argument has to be a odd number pair
cv.imshow('Blured park', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175) # cv.Canny(img, 125, 175)
cv.imshow('Canny edges', canny)

# dilating the image
dilated = cv.dilate(canny, (7, 7),  iterations = 5)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (7, 7), iterations = 5)
cv.imshow('Eroded', eroded)

# resize 
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400] # [vert dir, horz dir]
cv.imshow('Cropped', cropped)

cropped2 = img[50:200, 300:500]
cv.imshow('Cropped2', cropped2)

cropped3 = img[150:300, 200:400]
cv.imshow('Cropped3', cropped3)





##########
cv.waitKey(0)