import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0);
#The codec we are going to use
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#output file
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while True:
    #"Frame" will get the next frame
    #in the camera (via "cap")
    #"Ret" will obtain return value from getting the camera frame
    # either true of false
    ret, frame=cap.read();
    cv2.imshow("Video",frame)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow("Video2", grey)
    if cv2.waitKey(1)  == ord('q'):
        break
#.release() is to save changes
cap.release()
out.release()
cv2.destroyAllWindows()
