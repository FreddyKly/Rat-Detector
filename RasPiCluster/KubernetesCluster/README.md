# Cluster Setup and Installation 
This manual explains how to install the kubernetes distribution k3s on a set of RaspberryPi 3B+.  
The k3s distribution can be found on https://k3s.io/. 
A large part of this installation manual originates from this [tutorial](https://medium.com/thinkport/how-to-build-a-raspberry-pi-kubernetes-cluster-with-k3s-76224788576c). 

## Hardware Requirements 
The follwing hardware is required during this manual:
* At least 2 RaspberryPi 3b+
* An external SSD connected via USB
* Administrator access to the router of your network
* LAN- and powercables for the raspberries

## Preparations

The first step is to install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC. Other imagers do work to flash the OS image on the micro SD memory cards, but this has two advantages. This imager has the RaspberryPi operatingsystems already preselected. It also has an "advanced settings" menu, which can be used to give a hostname to the raspberry, activate SSH, give a username and a password, and set up the Wifi connection to your network. This means one has to just plug the micro SD card into the raspberry after flashing it.
The operating system we are using is **Raspberry PI OS (32-BIT)**. The main reason for using a 32-Bit architecture is to reduce the overhead, since the Raspberry Pis have a low computational to the servers used in a datacenter.
It seems reasonable to give the devices a hostname equivalent to their purpose. For example "masternodeX" or "workernodeX". This setup was build with one masternode and three workernodes. Therefore we named the devices: 
* masternode1
* workernode1
* workernode2
* workernode3

In the following the "masternode1" is just referenced by "masternode". Plug in the flashed micro SD cards, connect the Raspberrys via LAN to your network and turn them on. Now check if the devices are in your network. If the devices are in the network continue with the installation

## Installation of k3s

At first execute the following command on each of the raspberries to update the software:

`sudo apt update && upgrade`

This can be done simultaneously to reduce the waiting period. We start with the masternode and execute the following command:

`curl -sfL https://get.k3s.io | sh -`

During the installation an error will occur, but the installation itself wont be interrupted. Thus execute:

`sudo nano /boot/cmdline.txt`

This opens the cmdline.txt document in a texteditor. The document has only one line and needs to be enhanced by:

`cgroup_memory=1 cgroup_enable=memory`

It is important to not leave the first line and accidentaly insert a line break. Before the masternode is rebooted we have to get the node-token. Hence:

`sudo cat /var/lib/rancher/k3s/server/node-token`

This string is important for the installation of the worker nodes. Hence it has to be temporarily safed somewhere. After that reboot the masternode and continue with the workernodes.

`sudo reboot`

The installation of the workernodes is almost identical



