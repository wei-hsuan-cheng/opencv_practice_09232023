import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


# averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average blur', average)


# Gaussian blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian blur', gauss)


# median blur (better than averaging or even Gaussian blur, used in advanced CV)
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)


# bilateral blur (most effective, used in advanced CV)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)

##########
cv.waitKey(0)