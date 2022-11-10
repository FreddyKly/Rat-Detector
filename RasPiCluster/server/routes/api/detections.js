const express = require('express');
const mongodb = require('mongodb');

const router = express.Router();

// Get
// get the list of all RatDetections
router.get('/', async (req, res) => {
    const ratDetections = await loadRatDetectionCollection();
    res.send(await ratDetections.find({}).toArray());
})

async function loadRatDetectionCollection() {
    const client = await mongodb.MongoClient.connect('mongodb+srv://freddykly:RatDetector@cluster0.4wp40qf.mongodb.net/?retryWrites=true&w=majority', {useNewUrlParser: true});

    return client.db('cluster0').collection('ratDetections');
}

// Post
// Save a RatDetection to the database
router.post('/', async (req, res) =>{
    const ratDetections = await loadRatDetectionCollection();
    await ratDetections.insertOne({
        text: req.body.text,
        createdAt: new Date()
    });
    res.status(201).send()
});

// Delete
// Delete a RatDetection from the Database by ID
router.delete('/:id', async (req, res) =>{
    const ratDetections = await loadRatDetectionCollection();
    await ratDetections.deleteOne({
        _id: new mongodb.ObjectId(req.params.id)
    });
    res.status(200).send()
});

module.exports = router;