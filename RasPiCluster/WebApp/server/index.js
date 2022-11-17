const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

const app = express();

//Middleware
app.use(bodyParser.json({limit: "10mb", extended: true}));
app.use(cors());

const detections = require('./routes/api/detections');

app.use('/api/detections', detections);
app.use(express.json({limit: "10mb", extended: true}))
app.use(express.urlencoded({limit: "10mb", extended: true, parameterLimit: 50000}))

const port = 5000

app.listen(port, () => console.log(`Server started on port ${port}`));