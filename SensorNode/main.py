import base64
from io import BytesIO
import json
import os
from PIL import Image
import time
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
    print("Trying to send...")
    response = requests.post("http://iser-net.selfhost.co:30500/api/detections", headers=headers, data=imageMetaDataJSON)

    if(response.status_code == 201):
        print('Success')
    else:
        print(response)

"""
Provides the Image as encoded base64
"""
def provideEncodedImage(img):
    return base64.encodebytes(img).decode('utf-8')

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def main():  

    model = torch.hub.load('ultralytics/yolov5', 'custom', 'weights/best.pt', force_reload=True)

    model.conf = 0.5
    while True:
        try:
            time.sleep(2)

            img = "picture.jpg"

            results = model(img)

            print(results.pandas().xyxy[0])

            numberOfRats = 0
            confidence = []

            pred = results.pandas().xyxy[0]

            for index, row in pred.iterrows():
                if row['confidence'] > 0.5:
                    numberOfRats += 1
                    confidence.append(row['confidence'])

            print("Number of Rats detected: " + str(numberOfRats))
            print("Confidence: " + str(confidence))

            confidence = 0.9

            results.ims  # array of original images (as np array) passed to model for inference
            results.render()  # updates results.ims with boxes and labels

            
            if numberOfRats > 0:            
                for im in results.ims:
                    buffered = BytesIO()
                    im_base64 = Image.fromarray(im)
                    im_base64.save(buffered, format="JPEG")
                    encodedImg = base64.b64encode(buffered.getvalue()).decode('utf-8')
                    sendImageMetaData(encodedImageData=encodedImg, confidence=confidence, numberOfRats=numberOfRats)

            # timeStamp = 
        except IOError as e:    
            print('Race Condition occured')


if __name__ == "__main__":
    main()