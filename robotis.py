import cv2
import imutils
import numpy as np
import cv2
from sms import send_sms
cap = cv2.VideoCapture('http://192.168.110.86:8000/stream.mjpg')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

person_detected = 0

while cap.isOpened():
    ret, image = cap.read() 
    
    if ret:
        image = imutils.resize(image, width=min(400, image.shape[1]))

        (regions, _) = hog.detectMultiScale(image,winStride=(2, 1),padding=(4, 4),scale=1.05) #Histogram of Oriented Gradients 

        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h), 
                          (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_TRIPLEX
            cv2.putText(image,'intruder',(x,y-10), font, 0.5, (0,0,255))
        if len(regions) != 0:
            cv2.imwrite('frame.png', image)
            print("detected")
            person_detected += 1
        if person_detected >= 1:
            send_sms()
            print("sms")
            person_detected-=1
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()