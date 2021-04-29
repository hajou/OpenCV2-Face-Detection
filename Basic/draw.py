import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color 
#blank[200:300,300:400]=255,0,0
#cv.imshow('Bleu', blank)


# 2.draw rectangle 
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(255,0,0),thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0),thickness=-1)
cv.imshow('Cercle',blank)

# 4. Draw a line
cv.line(blank, (0,0), (300,400), (255,255,255), thickness=3)
cv.imshow('Line',blank)

# 5. Write text 
cv.putText(blank, 'hello',(300,255) ,cv.FONT_HERSHEY_TRIPLEX, (1.0), (0,255,0))
cv.imshow('text', blank)



cv.waitKey(0)