import cv2 as cv

def rescalerFrame(frame, scale=0.70):
    #images,Videos and Live Videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# resolution 
def changesRes(width,height):
    # Live Videos 
    capture.set(3, width)
    capture.set(4, height)
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescalerFrame(frame,scale=.8)
    cv.imshow('Video', frame)
    cv.imshow('videos rezised', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
