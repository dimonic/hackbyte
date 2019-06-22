# import Libraries
import numpy as np
from SetResolution import ChangeRes
import cv2

# Initialize Device
cam 		= 		cv2.VideoCapture(1)


# Set Resolution
# cam 		= 		ChangeRes(cam, 1280, 720)
cam 		= 		ChangeRes(cam, 1944, 2592)


# Start reading frames
while(True):
    ret, frame = cam.read()

    cv2.imshow('frame',frame)
    print(frame.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release Device
cam.release()
cv2.destroyAllWindows()