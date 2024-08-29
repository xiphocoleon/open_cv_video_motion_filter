import cv2 as cv
video = cv.VideoCapture('C:\\Users\\ThomasWilk\\Desktop\\20240426_150448.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(200, 50)

while True:
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)
        
        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture('C:\\Users\\ThomasWilk\\Desktop\\20240426_150448.mp4')
        
cv.destroyAllWindows()
video.release()
