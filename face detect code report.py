import cv2

#loading the pre-trained Haar Cascade for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#initialize the webcam
cap=cv2.VideoCapture(0)

while True:
    #read the face in the webcam
    ret,frame=cap.read()

    if not ret:
        break
    #convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces in the frame
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

    #draw rectangles around the dtect faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    #display the frame with detected face
    cv2.imshow('Face Detection',frame)

    #exit the loop when 'v' key is pressed
    if cv2.waitKey(1) & 0xFF ==ord('v'):
        break

#release the webcam and close the opencv window
cap.release()
cv2.destroyAllWindows()
    
