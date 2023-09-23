import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

# split
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# the larger concentration of a certain BGR color, the whiter will be in the split image


# merge
merged = cv.merge([b, g, r])
cv.imshow('Merged image', merged)

##########
cv.waitKey(0)