import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

while(cap.isOpened()):
    ret,frame = cap.read()
    grayImage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage,1.1,4)
    count=1
    keyPressed = cv2.waitKey(1)

    for x,y,w,h in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),3)
        smiles = smile_cascade.detectMultiScale(grayImage,1.8,15)
        for x,y,w,h in smiles:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
            print("Image "+str(count)+" Saved")
            path=r'C:\Users\Yash Phatak\Downloads\smiles\img'+str(count)+'.jpg'
            cv2.imwrite(path,img)
            count+=1
            if(count>=1): break
    cv2.imshow('live video',img)
    if(keyPressed & 0xFF==ord('q')):
        break
cap.release()                                  
cv2.destroyAllWindows()

