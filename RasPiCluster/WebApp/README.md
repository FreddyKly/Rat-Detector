# Setup with Docker (Prod. and Testing)
## Docker-compose
This is the easiest way of getting everything up and running.
Install Docker with docker-compose (https://docs.docker.com/compose/install/).
To check if the installation worked use <code>docker -v</code> and <code>docker-compose -v</code> in a Terminal.
<br>
<br>
<b>If you try to run the <ins>docker-compose on a RaspberryPi</ins> (not been tested so far [only thing that has been tested was to [build](#build-docker) and [run](#run-docker) the Container individually) then make sure to uncomment line 4 and 13 ("platform: linux/arm64") in the docker-compose.yml, to ensure the Image is build for the correct architecture.</b>

- Open a Terminal and navigate to the correct directory:
```
cd RasPiCluster/WebApp
```
- Enter:
```
docker-compose up
```

- This should build the docker images and then let them run. Server will be running on localhost:5000 and the client on localhost:8080.
After this command wait for everything to download and install (maybe 5min) and the go to localhost:8080 on your browser. The Web-App should be up and running.

- You're Done! Yay!

<hr>

## <a name="build-docker"></a>Build Docker Image (For a RaspberryPI [for native machine leave "--platform linux/arm64" out])
<b>This step will not be necessary if [this](#docker-compose) already worked</b>

Execute the following command from the root of this project:

#### Client

```
docker image build --platform linux/arm/v7 -t web-app-client:0.0.1 ./RasPiCluster/WebApp/client
```

#### Server

```
docker image build --platform linux/arm/7 -t web-app-server:0.0.1 ./RasPiCluster/WebApp/server
```

### <a name="run-docker"></a>Run Docker Image

#### Client 

Execute the following command from the root of this project:

```
docker run -p 8080:8080 web-app-client:0.0.1
```

#### Server 

Execute the following command from the root of this project:

```
docker run -p 5000:5000 web-app-server:0.0.1
```


### Npm installations 
1. Change directory
```
cd RasPiCluster/WebApp/server
```

2. Install dependencies for server
```
npm install
```

3. Change directory into the client
```
cd ../client
```

4. Install dependencies for the client
```
npm install
```

<br></br>

# Start the server:
1. Change Directory
```
cd RasPiCluster/WebApp/server
```

2. Start the Server on localhost:5000
```
npm run dev
```

<br></br>

# Start the Front-end
1. Change directory into client
```
cd RasPiCluster/WebApp/client
```

2. Start the Front-end on localhost:8080
```
npm run serve
```
