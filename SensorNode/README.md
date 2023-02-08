# Main Script with docker

The sensor node runs on Raspberry Pi OS Bullseye (64-bit), installed by inserting the SD-card into a computer and installing the OS by using Raspberry Pi Imager application.

To run the main script, execute in Rat-Detector/SensorNode:

```
docker compose up
```

# Camera Script

The camera script is running on the Python distribution(Version 3.9) of the Raspberry 4 to satisfy the requirements of the picamera2 library.

Set up:

```
pip install picamera2
pip install time
```

To run the camera script:

```
python /path/to/run_camera.py
```

# Telegram Bot

The Telegram Bot aimes to provide a direct and intuitive user notification system. The Python bot is integrated into the sensor node. The user has to subscribe to the Telegram channel "RatDetectionBot". Every new user is added automatically and will receive pictures of detected rats including information about the number of rats as well as the corresponding confidences. Furthermore, every random input message activates a personalized menu. It has two selectable options. The first one is toggling the notification on and off. This way, the user can deactivate the automatized sending of rats. The second option is the modification of the notification interval. To prevent permanent sending of rat notifications if a rat is recognized over a long time span, the sending interval between two pictures can be typed in. The Bot provides an accompanying input string control. By default, the alert is turned on and the notification interval is 600 seconds (10 minutes). Every user has individual settings.  
