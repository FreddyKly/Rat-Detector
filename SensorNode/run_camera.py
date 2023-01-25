from picamera2 import Picamera2, Preview
from libcamera import controls
import time

picam2 = Picamera2()
camera_config = picam2.create_still_configuration({"size": (2464, 2464)})
picam2.configure(camera_config)

camera_config = picam2.create_preview_configuration({"size": (2464, 2464)})
picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)

picam2.start(show_preview=True)
print("Camera started")

time.sleep(2)

while True:
    try:
        picam2.capture_file("picture.jpg")
        time.sleep(2)
        
    except KeyboardInterrupt:
        picam2.close()
        print("Camera closed")
        raise