#Drawing geometric shapes on images
import cv2
import numpy as np

img = cv2.imread('mypic.jpeg',1)
#img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(255,255),(0,255,0),5) #Variables - input,coordinates[start-end],*BGR* colring,thickness
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1) #the first co-ordinate is upper left of rectangle and the second one is the lower right
#for rectangle if we provide -1 instead of thickness then we fill the box

img = cv2.circle(img,(447,65),44,(0,255,0),-1)

font = cv2.FONT_HERSHEY_COMPLEX #font argument
img = cv2.putText(img,'Yash Phatak',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

