# face_detection
This is a python project in which we can detect many faces at the same time using live camera/webcams.
In this model, we will use opencv library which you can install in cmd.


Step1:- Importing OPENCV library: We need to install this library first. For this, we need to go open CMD and write command:
pip install opencv-python
Writing this command will help you to install the library after installation you can open new python file and import cv2.


Step2:- Loading the pre-trained haar cascade file for face detection
We will take a variable named face_cascade in which we will load or read the pre-trained files using Cascade Classifier function.

Step3:- Now we need to initialize the webcam, this open we will take a variable named as cap in which we will pass the code using Video capture function and will pass 0 as an argument as its index.

Step4: Now we will use a while loop in which we have stated if true then capture the webcam otherwise, break.

Step5:- Now, we will change the face detected into grey scale as face detection works efficiently in grey and black colours to do that we have used various functions.

Step6:- now we will detect the faces in the webcam or in the frame. Using the function detectmultiscale in which 4 arguments are passed i.e. gray, scaleFactor, minNeighbor and minSize. These are important arguments to be passed scaleFactor value must be within 1 to 1.5 whereas minNeighbors can be anything but is the difference between the pixels of two different faces and minSize is the minimum size of the face in order to be recognized or detected.

Step7:- Now it’s the time to draw the rectangles around the faces detected. In this we will set the size or pass the default arguments of size of rectangles i.e. x,y,w,h; these are the 4 measurements [cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2) ] these needed to be passed here 0,255,0 determines the colour of the rectangle. Whereas 2 determines the thickness of the rectangles.

Step8:- To end with the face detection, we need to show the face and the rectangle which is used to detect the face. For which we will use the function cv2.imshow ( ) here show will show us the frame of the webcam by passing 2 arguments i.e. ‘Face detection’ and variable frame.

Step9: At last when we need to terminate the loop it will go match the ASCII codes of the two different variables. In my project, I have used ‘v’ to terminate the loop. We have used 2 arguments i.e. wait key in which we have passed 1 as the millisecond time to pause the loop and when the 0xFF 8 bit ASCII code will match the ASCII code of ‘v’, ultimately the loop will get terminated.

Step10:- In last when we need to end the program we will release the cap and will command cv2 to destroy all the windows using this command or code;
cap.release ()
cv2.destroyAllWindows ()
