from api.firebase import firebase
import json

from device.camera.picture import picture

print(picture.get_file_path())
print(picture.folder_name)
print(picture.file_name)

firebase.upload_file('test/test.jpg', '/home/pi/green-house-control/data/picture/2023-04-22/2023-04-22__09-55-02__picture.jpg')
#firebase.upload_file(picture.get_blob_name(), picture.get_file_path())


