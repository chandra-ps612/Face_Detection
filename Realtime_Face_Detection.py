import cv2
import numpy as np 

output_videoPath='C:\\Users\\lav singh\\workplace\\Face_Detection\\output_video.mp4'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
create=None
cap=cv2.VideoCapture(0)
while True:
    _, frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_frame,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)
    cv2.imshow('Output', frame)
    if create is None:
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        create = cv2.VideoWriter(output_videoPath, fourcc, 3, (640, 480), True)
    create.write(frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cap.release()
create.release()
cv2.destroyAllWindows()