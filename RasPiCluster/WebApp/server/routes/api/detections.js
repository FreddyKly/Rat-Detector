const express = require('express');
const pool = require('../../DBConnector/db_connector');

const router = express.Router();


// Returns the rows of the "detection" table
async function loadDetections() {
    try{
        const selectAllQuery = 'SELECT * FROM detections';

        con = await pool.getConnection();

        const detections = await con.query(selectAllQuery);

        console.log('Detections were queried successfully! Number of Detections: ', detections.length);

        return detections;

    } catch (error) {
        throw error;
    } finally {
        if (con) return conn.end();
    }
        
}

// Get
// get the list of all detections
router.get('/', async (req, res) => {
    try {
        console.log('Registered a Get-Request!')

        const detections = await loadDetections();

        // console.log('Detections: ', detections)

        res.send(await detections);

    } catch (error) {
        res.status(400).send(error.message);
    }
    
})

// Post
// Save a Detection to the database
router.post('/', async (req, res) =>{
    try {
        console.log('Registered a POST-Request')

        con = await pool.getConnection();

        const insertQuery = 'INSERT INTO detections VALUES (?, ?, ?, ?, ?)';

        const result = await con.query(insertQuery, [null, req.body.image, new Date(), 2, 95]);

        res.status(201).send('Entry was successfully inserted!');

    } catch (error) {
        res.status(400).send(error.message);
    } finally {
        if (con) return con.end();
    }

    
});

// Delete
// Delete a Detection from the Database by ID
router.delete('/:id', async (req, res) =>{
    const ratDetections = await loadDetections();
    await ratDetections.deleteOne({
        _id: new mongodb.ObjectId(req.params.id)
    });
    res.status(200).send()
});

module.exports = router;