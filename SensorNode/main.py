import base64
import json
import os

import requests

"""
Assamble all the necessary datapoint and send them to the Back-end
"""
def sendImageMetaData(encodedImageData, confidence, numberOfRats):
    imageMetaData = {
    "image": encodedImageData,
    # "timeStamp": timeStamp,       Discuss if timestamp should be provided by Front- or Back-end
    "confidence": confidence,
    "numberOfRats": numberOfRats
    }

    imageMetaDataJSON = json.dumps(imageMetaData)

    headers = {'Content-type': 'application/json'}

    response = requests.post("http://localhost:5000/api/detections", headers=headers, data=imageMetaDataJSON)

    if(response.status_code == 201):
        print('Success')

"""
Provides the Image as encoded base64
"""
def provideEncodedImage():
    with open('SensorNode/oikawa.jpg', mode='rb') as file:
        img = file.read()
    return base64.encodebytes(img).decode('utf-8')

"""
Provides the confidence level
"""
#TODO: What about confidence Levels for multiple Rats?
def provideConfidence():
    return 0.95
    
"""
Provides the number of Rats found in the image
"""
def provideNumberOfRats():
    return 2

def main():
    encodedImg = provideEncodedImage()
    # timeStamp = 
    confidence = provideConfidence()
    numberOfRats = provideNumberOfRats()
    sendImageMetaData(encodedImageData=encodedImg, confidence=confidence, numberOfRats=numberOfRats)


if __name__ == "__main__":
    main()