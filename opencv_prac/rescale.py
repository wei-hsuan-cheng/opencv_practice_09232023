import cv2 as cv

########## Rescaling
def rescaleFrame(frame, scale = .2):
    # images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

########## Changing resolution
def changeRes(width, height):
    # live videos
    capture.set(3, width)
    capture.set(4, height)


########## Reading images and videos
# reading images
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img)
cv.imshow('Cat Resized', resized_image)
cv.waitKey(0)

# reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindow()