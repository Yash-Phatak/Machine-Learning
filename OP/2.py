#How to show videos from Camera
import cv2

cap = cv2.VideoCapture(0) #if video file then 'video.mp4'

#4CC code is used to check videos codac
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))  # Arguments - video_name,fourcc,number_of_frames,size    

#while(cap.isOpened()) to check if file path or index is correct

while(cap.isOpened()):
    ret,frame= cap.read()
    if ret == True:
        #reading properties of the Frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break

cap.release()
out.release()
cv2.destroyAllWindows()
