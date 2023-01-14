import axios from 'axios';
//const url = 'http://localhost:5000/api/detections';
  const url = 'http://192.168.188.26:30500/api/detections';
class detectionsService {
    // Get detections
    static getDetections() {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.get(url);

                console.log('There was a Response to the Get-Request: ', res)

                const data = res.data;

                resolve(
                    data.map(detection => ({
                        ...detection,
                        createdAt: new Date(detection.createdAt),
                        showDetails: false
                    })
                ));
                
            } catch(err) {
                reject(err);
            }
        })
    }

    // Create detections
    static insertDetection(text) {
        return axios.post(url, {
            text: text
        });
    }

    // Delete Detections
    static deleteDetection(id) {
        return axios.delete(`${url}/${id}`)
    }
}

export default detectionsService;