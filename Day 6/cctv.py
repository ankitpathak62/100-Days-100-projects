import cv2
from datetime import datetime
import os

cap = cv2.VideoCapture(0) 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

if not os.path.exists('detections'):
    os.mkdir('detections') # make sure you have a detections folder
    
while True:    
    _, frame = cap.read()    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)    
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, width, height) in faces:    
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
        face_roi = frame[y:y+height, x:x+width]
        if not os.path.exists('detections/' + datetime.now().strftime('%Y-%m-%d')):
            os.mkdir('detections/' + datetime.now().strftime("%Y-%m-%d"))

        cv2.imwrite('detections/' + datetime.now().strftime("%Y-%m-%d") + '/' + datetime.now().strftime("%H-%M") + '.jpg', face_roi)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break