# import Libraries
import cv2
from SetResolution import ChangeRes
from PIL import Image
import numpy as np
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

# Initialize Device
cam 		= 		cv2.VideoCapture(1)


# Set Resolution
cam 		= 		ChangeRes(cam, 1280, 720)
# cam 		= 		ChangeRes(cam, 2592, 1944)


# Start reading frames
for i in range(2):
# while True:
    ret, frame 	= 	cam.read()
    array 		= 	cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    img 		= 	Image.fromarray(array)
    img.save('./temp/sample.png')
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release Device
cam.release()
cv2.destroyAllWindows()


# try:
#     # Create the BlockBlockService that is used to call the Blob service for the storage account
#     block_blob_service = BlockBlobService(account_name='produceimages', account_key='m8BZlDWt8wDI+wHPVwyhzyKCeMDz53GKy73o6sA5u57PyyTN1tvQg9pv4BRDBCOdlBEkKbb5pKu15fUTP59sNg==')

#     # Create a container called 'quickstartblobs'.
#     container_name ='quickstartblobs'
#     block_blob_service.create_container(container_name)

#     # Set the permission so the blobs are public.
#     block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

#     # Create a file in Documents to test the upload and download.
#     local_path=os.path.expanduser("./temp/")
#     local_file_name = "sample.png"
#     full_path_to_file =os.path.join(local_path, local_file_name)

#     print("\nUploading to Azure" + local_file_name)

#     # Upload the created file, use local_file_name for the blob name
#     block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

#     sys.stdout.flush()
#     input()

#     # Clean up resources. This includes the container and the temp files
#     # block_blob_service.delete_container(container_name)
#     os.remove(full_path_to_file)
    
# except Exception as e:
#     print(e)






