import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -100, 200)
cv.imshow('Translated', translated)


# rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated_wrong = rotate(rotated, -45) # don't do this
cv.imshow('Rotated_rotated_wrong', rotated_rotated_wrong)

rotated_rotated = rotate(img, -90) # except, do this
cv.imshow('Rotated_rotated', rotated_rotated)


# resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# flip
flipped = cv.flip(img, -1) # 0: hor-axis, 1: ver-axis, -1: both the 2 axis
cv.imshow('Flipped', flipped)


# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



##########
cv.waitKey(0)
