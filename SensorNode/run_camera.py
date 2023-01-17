from picamera2 import Picamera2, Preview
from libcamera import controls
import time


picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size": (640, 640)})
picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)

picam2.start(show_preview=True)
print("Camera started")
#picam2.set_controls({"AfMode": 2, "AfTrigger": 0})
time.sleep(4)

while True:
    try:
        picam2.capture_file("picture.jpg")
        time.sleep(2)
    except KeyboardInterrupt:
        picam2.close()
        print("Camera closed")
        raise