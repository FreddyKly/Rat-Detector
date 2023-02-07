# Rat-Detector

## Project Description 
The goal of the project was to develop an edge computing solution for the automatic detection of pest [as defined here](https://www.christianbaun.de/CGC2223/index.html). Therefore we had to:
* setup a Kubernetes Cluster
* setup a Sensor-Node
* detect pests with the Sensor-Node
* send the pictures to the Cluster
* store the pictures on the cluster 
* display the pictures in a WebApp
* optional: notify user via Telegram bot when a pest is detected

## Tech-Stack 
* YOLOv5
  * Object detection
  * [ReadMe](./SensorNode/weights/README.md) 
* Docker / Python
  * to run applications on the Sensor-Node
  * [ReadMe](./SensorNode/README.md)
* K3S
  * Kubernetes distribution for Cluster
  * [ReadMe](./RasPiCluster/KubernetesCluster/README.md)
  * The ReadMe contains a detailed description of purpose and function of the images below
  * MariaDB 
  * NFS-Server 
* Webapp
  * NodeJS/ExpressJS
  * Vue
  * [ReadMe](./RasPiCluster/WebApp/README.md)




