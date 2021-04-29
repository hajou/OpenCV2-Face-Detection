from cv2 import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR --> HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR --> L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR --> L*u*v
luv = cv. cvtColor(img,cv.COLOR_BGR2Luv)
cv.imshow('Luv', luv)



cv.waitKey(0)