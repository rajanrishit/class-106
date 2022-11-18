# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()


    #convert to grayscale
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect the faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grey,1.1,4)
    #draw the rectangle around each face
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()