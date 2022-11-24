FROM ultralytics/yolov5:latest

WORKDIR /Sensor-Node

COPY main.py ./
COPY requirements.txt ./
COPY ushikawa.jpg ./
COPY weights/ ./weights/

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "-m", "main" ]