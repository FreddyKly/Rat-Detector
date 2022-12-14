# Install dependencies (on local native machine)
Go to the requirements.txt and delete the hashtag before "torch" when dependecies are not being installed in a docker container

```
pip install -r requirements.txt
```

and follow this tutorial for installing ultralytics: https://github.com/ultralytics/yolov5/blob/master/README.md

# Build Docker Image (On a RaspberryPI, for native machine leave "--platform linux/arm64" out)
Execute the following command from the root of this project:

```
docker image build --platform linux/arm64 -t sensor-node:0.0.1 ./SensorNode
```

# Run Docker Image
Execute the following command from the root of this project:

```
docker run --network="host" sensor-node:0.0.1
```
