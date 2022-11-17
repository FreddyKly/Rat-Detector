import base64
import json
import os

import requests
import torch


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
    else:
        print(response)

"""
Provides the Image as encoded base64
"""
def provideEncodedImage():
    with open('ushikawa.jpg', mode='rb') as file:
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

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def main():
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'weights/best.pt', force_reload=True)

    #bild von camera
    img = '../../test_pi_camera/Rat_5.jpg'  # or file, Path, PIL, OpenCV, numpy, list

    results = model(img)

    results.ims  # array of original images (as np array) passed to model for inference
    results.render()  # updates results.ims with boxes and labels
    for im in results.ims:
        buffered = BytesIO()
        im_base64 = Image.fromarray(im)
        im_base64.save(buffered, format="JPEG")
        print(base64.b64encode(buffered.getvalue()).decode('utf-8'))  # base64 encoded image with results

    encodedImg = provideEncodedImage()
    # timeStamp = 
    confidence = provideConfidence()
    numberOfRats = provideNumberOfRats()
    sendImageMetaData(encodedImageData=encodedImg, confidence=confidence, numberOfRats=numberOfRats)


if __name__ == "__main__":
    main()