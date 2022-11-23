FROM python:3.9

WORKDIR /Sensor-Node

COPY main.py ./
COPY requirements.txt ./
COPY weights/ ./weights/

RUN python3 -m pip install -r requirements.txt

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git

RUN git clone https://github.com/ultralytics/yolov5
RUN cd yolov5
RUN pip install -r requirements.txt

CMD [ "python3", "-m", "main" ]
