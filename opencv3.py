#Drawing and writing on images!!
import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#where to draw, start,end ,color , width
cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
#the -1 fills the circle!
cv2.circle(img,(447,63), 63, (0,255,0), -1)
#polygons!
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
#True de bt2oli hal ana 3awez a-connect w a2fel el shape wala la2
cv2.polylines(img, [pts], True, (0,255,255), 3)

#el font elly hst5dmo
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()