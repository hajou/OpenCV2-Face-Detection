import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade
canny = cv.Canny(blur,125, 175)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3),iterations=1)
cv.imshow('dilating', dilated)

# Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroding',eroded)

#Resize
resize= cv.resize(img, (500,500),interpolation = cv.INTER_CUBIC)
cv.imshow('Resize',resize)

# Cropping
cropped = img [50:200,200:400]
cv.imshow('Cropping img', cropped)



cv.waitKey(0)