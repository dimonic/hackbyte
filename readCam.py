# import Libraries
import numpy as np
import cv2

# Initialize Device
cap = cv2.VideoCapture(1)


# Start reading frames
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release Device
cap.release()
cv2.destroyAllWindows()