import cv2
img = cv2.imread('mypic.jpeg',0) #0-grayscale

print(img)

cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows() #destroyWindow for particular
#value
cv2.imwrite('yash_copy.png',img) 