#INITIAL SETUP
#----------------------------------------------------------------
#importing required libs
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np0

#rolling intro
intro = cv2.imread('frames\img1.jpeg')

#badluck restinpeace
kill = cv2.imread('frames\img2.jpeg')

#ok fine you made it
winner = cv2.imread('frames\img3.png')

cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Display frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)

#sets the minimum confidence threshold for the detection
net.setInput(blob)
output_layers = net.getUnconnectedOutLayersNames()
outputs = net.forward(output_layers)
conf_threshold = 0.5

# Loop over all detections and draw bounding boxes around objects with confidence above threshold
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > conf_threshold:
            # Draw bounding box around object


#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
sqr_img = cv2.imread('img\sqr(2).png')
mlsa =  cv2.imread('img\mlsa.png')
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
    while True:
        #show the loss screen from the kill image read before and end it after we press q

else:
#WIN SCREEN
#show the win screen from the winner image read before

    while True:
        #show the win screen from the winner image read before and end it after we press q

#destroy all the windows