# Main Script with docker

To run the main script do in Rat-Detector/SensorNode:

```
docker compose up
```

# Camera Script

The camera script is running on the Python ditribution(Version 3.9) of the Raspberry 4 to satisfy the requirements of the picamera2 library.

Set up:

```
pip install libcamera?
pip install picamera2
pip install time?
```

To run the camera script:

```
python /path/to/run_camera.py
```
