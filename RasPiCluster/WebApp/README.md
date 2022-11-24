# Setup
## Installations
### MongoDB Database
Follow Tutorial under: https://www.mongodb.com/basics/mongodb-atlas-tutorial
The Names of the databases and users are hardcoded right now. To use your own database name/username/password you would need to make adjustments in the code base under: Rat-Detector/RasPiCLuster/server/routes/api/detections.js. If you just want to run the code, here is what I used:
- Database name: cluster0
- username: freddykly
- password: RatDetector

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
cd RasPiCluster
```

2. Start the Server on localhost:5000
```
npm run dev
```

<br></br>

# Start the Front-end
1. Change directory into client
```
cd RasPiCluster/client
```

2. Start the Front-end on localhost:8080
```
npm run serve
```

# Build Docker Image (On a RaspberryPI, for native machine leave "--platform linux/arm64" out)
Execute the following command from the root of this project:

```
docker image build --platform linux/arm64 -t web-app:0.0.1 ./RasPiCluster/WebApp
```

# Run Docker Image
Execute the following command from the root of this project:

```
docker run -p 8080:8080 -p 3000:3000 web-app:0.0.1
```