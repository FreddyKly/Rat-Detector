FROM python:3.9

WORKDIR /Sensor-Node

COPY main.py ./
COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "-m", "main.py" ]