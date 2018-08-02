import numpy as np
import cv2
import matplotlib.pyplot as plt

#Reads image from the computer
#cv2.imread('img', 0= grey , 1= color with no obaque , -1 unchanged)
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#create a window with name image and takes what to be displayed
cv2.imshow('image',img)
#waits for a key
cv2.waitKey(0)
#When key is pressed , close kol 7aga.
cv2.destroyAllWindows()


#plt.imshow(img, cmap='gray', interpolation = "bicubic")
#plt.show()
