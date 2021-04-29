from cv2 import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding 
threshold,thresh = cv.threshold(gray,100,255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

# Simple Reverse Thresholding
threshold, threshold_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Inv Threshold',threshold_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 7)
cv.imshow('Adaptive Thresholding',adaptive_thresh)

cv.waitKey(0)