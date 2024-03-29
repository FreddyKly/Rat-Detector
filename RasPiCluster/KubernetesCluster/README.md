# Cluster Setup and Installation 
This manual explains how to install the Kubernetes distribution k3s on a set of Raspberry Pi 3B and how to configure it for this project.  
The k3s distribution can be found on https://k3s.io/. 

## Hardware Requirements 
The following hardware is required during this manual:
* At least 2 Raspberry Pi 3B
* An external SSD hard drive
* Administrator access to the router of your network
* LAN- and power cables for the Raspberries

## Preparations

At first install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC. Other applications do also work to flash the OS image on the micro-SD memory cards, but this particular application has two advantages. The imager has the Raspberry Pi operating systems already available. It also has an "advanced settings" menu, which can be used to assign a hostname, enable SSH, assign a username and a password, and set up the Wi-Fi connection to your network. This means that you only have to plug the micro-SD card into the Raspberry after flashing.
The operating system we are using is **Raspberry PI OS Lite (32-
IT)**. The main reason for using a 32-Bit architecture is to reduce the overhead. Raspberry Pis have low computing power compared servers to used in a datacenter.
It seems reasonable to give the devices a hostname equivalent to their purpose, for example, "masternodeX" or "workernodeX". This setup was built with one masternode and three workernodes. Therefore, we named the devices: 
* masternode1
* workernode1
* workernode2
* workernode3

In the following the "masternode1" is just referenced by "masternode". Plug in the flashed micro-SD cards, connect the Raspberries via LAN to your network and turn them on. Now check if the devices are in your network. If the devices are in the network continue with the installation.

## Installation of a k3s-Cluster

A large part of this installation manual originates from this [tutorial](https://medium.com/thinkport/how-to-build-a-raspberry-pi-kubernetes-cluster-with-k3s-76224788576c). 
The next steps describe the installation of the cluster.\
Execute the following command on each of the raspberries to update and upgrade the software:

    sudo apt update && sudo apt upgrade -y

This can be done simultaneously to reduce the waiting period.\
After that execute the following command on the masternode:

    curl -sfL https://get.k3s.io | sh -

During the installation an error will occur, but the installation itself won’t be interrupted. Thus execute:

    sudo nano /boot/cmdline.txt

This opens the "cmdline.txt" document in a text editor. The document has only one line and must be extended by the following line:

    cgroup_memory=1 cgroup_enable=memory

It is important not to leave the first line and accidentally insert a line break. Before the masternode is rebooted we must get the node-token. Hence execute:

    sudo cat /var/lib/rancher/k3s/server/node-token

This string is important for the installation of the worker nodes.\
It must be temporarily saved somewhere. After that reboot the masternode and continue with the installation of the workernodes.

    sudo reboot

The installation of the workernodes is almost identical to the installation of the masternode. Install k3s with the following command and insert the masternode IP address and token in the marked fields:

    curl -sfL https://get.k3s.io | K3S_URL=https://<masternode_IP_Address>:6443 K3S_TOKEN=<masternode_token> sh -

Again, the installation will yield an error, but the procedure won´t be interrupted. Execute the same commands that were used at the masternode to correct the error. Reboot the workernode after that:

    sudo reboot

Repeat this installation process for every workernode. Whether the installation was successful can be checked by executing: 

    sudo k3s kubectl get nodes

If all nodes have the status "Ready" we can continue with the installation. 

## Configuration of the k3s-Cluster

The configuration of the cluster is based on the requirements of the project. Another aspect we considered are the limits of the hardware at hand. 
The cluster has to maintain persistent storage and display the results of the classification from the Sensor-Node in a WebApp. The limitations of the hardware are relevant in a later stage of the documentation. The configuration is applied to the cluster in form of a YAML manifest via the Kubernetes API. 
At the start we will explain our decision which lead to the final cluster architecture and hereafter the YAML manifest itself. 

### Theoretical Decisions and Application
By default, each node only accesses its own filesystem. There are several possibilities to create persistent storage for the Kubernetes cluster. The first possibility is to label the cluster nodes and specifically define the node on which each application must run. This procedure seems to be technical possible, but from our point of view it represents the exact opposite of the intended use of a Kubernetes cluster. The second option we considered was the object storage application [MinIO](https://min.io/). The last possibility we took into account was a NFS-Server hosted on the cluster.
To determine which of the two options works best, we split up the hardware. After a period of testing, we came to the conclusion that MinIO created too much overhead and therefore the application kept crashing the cluster nodes. Also during the MINIO setup we ran into a lot of issues concerning the pod in which it was supposed to run while the NFS-Server worked without a problem. Thus, our decision was mostly guided by pragmatism and led us to the use of the NFS-Server opposed to the implementation of the theoretically well suited MinIO. To enhance the available storage, we made use of an external SSD hard drive. The goal of this enhancement was to reduce the number of read/writes on the micro-SD card. We plugged the SSD into the masternode and bound the pod of the NFS-Server to the node with a label.

At first glance, this method seems to contradict our previous statement about the intended use of a Kubernetes cluster. But here we argue with the hardware limitations, a productive cluster could use a Network Attached Storage or one could configure predefined solutions for persistent storage. To the best of our judgment the Raspberries used here seemed to lack the capabilities to run MinIO and our applications in a manner suited for this project. An NFS-Server is like a NAS and since we only have one masternode we are not creating more single-points of failure.  

It has to be stated that our decision between the NFS-Server and MinIO might have been biased. During the project (after our testing period) we swapped the micro-SD cards of the MinIO nodes for newer ones. This led to an notable increase in performance. At this point in time, we already built on our earlier decision and a change was not easily possible anymore. Hence, we sticked to the NFS-Server.

To set up the NFS-Server the masternode has to be labeled with the command:

    sudo kubectl label node <masternode_hostname> SSD=enabled

Since we plugged the external SSD in via USB, we wanted to make sure it is always booted into a defined directory. Hence we extracted the UUID:
    
    sudo blkid

After that we inserted the following string into the file system table /etc/fstab

    UUID=<UUID_of_SSD>   /media/usb   ntfs   auto,nofail,sync,users,rw   0   0

After that reboot the device again with:

    sudo reboot

With this configuration the SSD is always mounted into the defined directory after a reboot. \
After that we copy the manifest directory to the masternode and apply it to the cluster with: 

    sudo kubectl apply -f ./manifest

To get the running pods, we can use the command: 

    sudo kubectl get pods -n work-space

Since we created our own namespace we have to extend the commands by "-n work-space". To get access to the MariaDB the following commands must be executed:

    sudo kubectl exec -it <Containername> -n work-space -- /bin/bash

This opens the bash of the pod with the MariaDB. To get the MariaDB console type:

    mariadb -p
 
Enter the password as requested. The password of the MariaDB is currently "password". 
It is saved in the "secret.yaml" file and is base64 encoded. Do not use this password in production.

### Kubernetes Manifest
The "manifest" directory has several files that are applied to the cluster with the kubectl API. These files are (mostly) named by their Kubernetes API kinds. It must be stated, that the "deployments.yaml" file also contains the "namespace" kind. Thus, the directory contains:
* deployments.yaml
* persistent_volume_claims.yaml
* persistent_volumes.yaml
* secrets.yaml 
* services.yaml 

The contents of these files originate from multiple sources. We will not explain every aspect of the configuration, but rather point out important and significant aspects of the architecture and setup. An important source for our configuration was the [Kubernetes documentation](https://kubernetes.io/docs/home/). We also used additional sources, but these will be mentioned in the specific sections.

For the configuration of the NFS-Server setup we also used [this article](https://github.com/shaposhnikoff/my_medium_articles_starred/blob/master/reliable-kubernetes-on-a-raspberry-pi-cluster-storage.md). The NFS-Server makes use of four Kubernetes API kinds. These are a "Service", a "Deployment", a "PersistentVolume" (PV) and a "PersistentVolumeClaim" (PVC).  

An important aspect of this configuration is the setup of persistent storage. At the start we created a PV. This represents a piece of storage which has been configured based on the given capacities. The "accessMode" defines the type of access and number of nodes that can mount it. The value "ReadWriteOnce" implies that only one node can mount the volume which than has read and write access. Under the "nodeSelectorTerms" we defined the label which is a selection criterion for the PV. Only one node has the external SSD and with this flag we can determine to which node the PV is assigned. The "path" attribute is mentioned because this path is mounted by the SSD. Hence the data of the NFS-Server is stored on the SSD. 

A PVC is the counterpart to the PV and thus necessary for our setup. The PVC represents a request for storage. The specifications of the request are defined in the "persistent_volume_claims.yaml". In our case it just contains the capacity. If the PV and the PVC are bound together, they represent a one-to-one mapping.

Deployments manage the "desired state" for pods. They are specific for one certain type of image. If the current state is not equal to the desired state, Kubernetes changes the current state until the desired state is reached. In this configuration, you can specify network settings or the number of simultaneously active pods. In "deployments.yaml" the "nfs-server" contains three important elements. The first element is the "nodeSelector" its purpose is equal to the "nodeSelectorTerm" of the PV. The second and third elements are the "volumes" and "volumeMounts" attributes. In the "volumes" attribute we defined the PVC as storage capacity for this deployment. In "volumeMounts" we mounted the  "volume" against the path "/exports". This means we indirectly mounted the directory /media/usb/share (defined when setting up the SSD and the PV) on the SSD into the NFS-Server. 

The last important element is the service. Kubernetes distributes IP addresses dynamically. In this specific case this behavior is not desired, hence we gave the pod a static IP address. 

The remaining configuration is used to do deploy the WebApp. It is composed out of three parts that are the MariaDB database, the WebApp-Server part and the WebApp-Client part. For this configuration we additionally used a example from the [Kubernetes documentation](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/). 

The WebApp uses a MariaDB as database. The reason for that are the following properties. MariaDB is available on a 32-Bit architecture, is relational and can be used to store images and it has a predefined connector to the nodeJS framework.

For MariaDB also exists a deployment. Similar to the NFS server we defined a "volume" and "volumeMounts". This time the "volume" was the NFS-Server which we mounted into the path where the MariaDB saves the data ("/var/lib/mysql"). This configuration displays the reason why we choose a static IP-Addresses when configuring the NFS-Server, it allows us to specify the IP address of the NFS-Server with certainty. A unique configuration in this setup is the "secrets.yaml" file. Under the "secretKeyRef" tag in the deployment we make use of an encrypted string, which is the password to the database itself. Secrets are used to divide confidential or sensitive data from the application code. Similar to the NFS-Server we also created a service which defined a static IP address for the database.

The remaining two deployments and services are used for the WebApp. The images of the WebApp are stored in the DockerHub. There were mainly two reasons to store the images there and these were the ease of use and the wide range of people using it. The deployments ensure, that one pod of the server- and client-part is always up and running. 
The remaining services are from the type "LoadBalancer". This service provides an IP address for the pods that can be accessed from outside of the cluster. We forward the ports of the pods to two distinct "nodeports". The "nodeports" have by default a range of 30000-32767, hence the high "nodeports". The IP address of the MariaDB is statically defined before the WebApp Image is compiled and pushed to DockerHub. Therefore, the images of the WebApp have to be recompiled with changed IP addresses in a new setup. 
