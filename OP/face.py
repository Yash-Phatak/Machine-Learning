import cv2

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Read the image
#image = cv2.imread('mypic.jpeg')

#Live Video Capturing
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame= cap.read()
    if ret == True:
        # Convert the image to grayscale    
        gray_image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image,
                                            scaleFactor=1.1,
                                            minNeighbors=5,
                                            minSize=(30, 30))

        # Print the number of faces detected
        print(len(faces))

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the image with the faces detected
        cv2.imshow('Image with faces detected', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else: break
cap.release()
cv2.destroyAllWindows()