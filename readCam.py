# import Libraries
import cv2
from SetResolution import ChangeRes
from PIL import Image
import numpy as np
import datetime
import time
from Azure import AzureUpload

# Initialize Device
cam 		= 		cv2.VideoCapture(1)

# Set Resolution
# cam 		= 		ChangeRes(cam, 1280, 720)
# cam 		= 		ChangeRes(cam, 2592, 1944)


# Start reading frames
for i in range(4):
# while True:
    ret, frame 	= 	cam.read()
    array 		= 	cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    img 		= 	Image.fromarray(array)
    st 			= 	datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # time.sleep(3)
    currentfile = 	'sample_'+st+'.png'
    img.save('./temp/'+currentfile)
    # cv2.imshow('frame',frame)
    AzureUpload(currentfile)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release Device
cam.release()
cv2.destroyAllWindows()








