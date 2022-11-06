import cv2
from flask import render_template, request
import mediapipe as mp
import numpy as np
from fitness_app import PoseModule as pm

cap = None
def main():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    direction = 0
    form = 0
    feedback = "Fix Form"
    while cap.isOpened():
        ret, img = cap.read() #640 x 480
        if not ret:
            break
        #Determine dimensions of video - Help with creation of box in Line 43
        width  = cap.get(3)  # float `width`
        height = cap.get(4)  # float `height`
        # print(width, height)
        
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            elbow = detector.findAngle(img, 11, 13, 15)
            body = detector.findAngle(img, 11, 23, 27)
            
            #Percentage of success of pushup

            #Check to ensure right form before starting the program
      
        
            #Check for full range of motion for the pushup
            if 85<=elbow <= 95 and 175<=body<=185:
                        feedback = "Good Form"
                        if direction == 0:
                            count += 0.5
                            direction = 1
            else:
                        feedback = "Fix Form"
                        
            
            #Draw Bar
            '''
            if form == 1:
                #cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                #cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
                cv2.rectangle(img, (int(width*.875), int(height*.1)), (int(width*.9), int(height*.8)), (190, 150, 37), 3)
                cv2.rectangle(img, (int(width*.875), int(bar/380*height*.8)), (int(width*.9), int(height*.8)), (190, 150, 37), cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (int(width*.851), int(height*.95)), cv2.FONT_HERSHEY_SIMPLEX, 3,(0, 0, 0), 10)
            '''

            #Pushup counter
            #cv2.rectangle(img, (int(width*.01), int(height*.01)), (int(width*.5), int(height*.1)), (190, 150, 37), cv2.FILLED)
            #cv2.putText(img, 'Pushup Counter: ' + str(int(count)), (int(width*.01), 80 ), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 10)
            
            #Feedback 
            #Feedback 
            if feedback == "Fix Form":
                cv2.rectangle(img, (int(width*.75), 0), (int(width*.97), int(height*.1)), (0, 40, 252), cv2.FILLED)
            else:
                cv2.rectangle(img, (int(width*.82), 0), (int(width*.96), int(height*.1)), (32, 255, 0), cv2.FILLED)
            cv2.putText(img, feedback, (int(width*.75), 80 ), cv2.FONT_HERSHEY_SIMPLEX, 3,(0, 0, 0), 10)
            
        temp, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
        '''    
        cv2.imshow('Pushup counter', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        '''
    cap.release()
    cv2.destroyAllWindows()
'''
if __name__ == "__main__":
    main()
'''