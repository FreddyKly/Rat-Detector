from picamera2 import Picamera2, Preview
import time


picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)

picam2.start()
print("Camera started")
time.sleep(4)

while True:
    try:
        picam2.capture_file("picture.jpg")
        time.sleep(2)
    except KeyboardInterrupt:
        picam2.close()
        print("Camera closed")
        raise