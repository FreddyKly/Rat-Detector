from picamera2 import Picamera2, Preview
import time

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size": (3280, 2464)})
picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)

picam2.start(show_preview=True)
#picam2.start()
print("Camera started")

time.sleep(2)

while True:
    try:
        picam2.capture_file("picture.jpg")
        time.sleep(2)
        print("Face")
    except KeyboardInterrupt:
        picam2.close()
        print("Camera closed")
        raise