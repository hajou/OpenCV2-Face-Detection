from cv2 import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Park',img)

# Average
average = cv.blur(img,(7,7))
cv.imshow('Average',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blau',gauss)

# Median Blur Reduce noise
median = cv.medianBlur(img, 7)
cv.imshow('Medin Blur',median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)