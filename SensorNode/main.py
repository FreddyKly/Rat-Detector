import base64
from io import BytesIO
import json
import os
from PIL import Image
import time
import requests
import torch
import urllib.request

OFFSET = 0
botToken = "6040873921:AAGQagXlzAY6kBTXuDyQWzySLl_Cq8d9xo4"

requestURL = "https://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "https://api.telegram.org/bot" + botToken + "/sendMessage"
sendPhotoURL = "https://api.telegram.org/bot" + botToken + "/sendPhoto"
picpath = r"/usr/src/app/sensor-node/detect.jpg"

# check for Telegram update
def update (url):
    global OFFSET
    try:
        update_raw = requests.get(url + "?offset=" + str(OFFSET))
        update = update_raw.json()
        result = extract_result(update)

        if result != False:
            OFFSET = result['update_id'] + 1
            return result
        else:
            return False

    except requests.exceptions.ConnectionError:
        pass


# extract result for update() function
def extract_result (dict):
    result_array = dict['result']

    if result_array == []:
        return False
    else:
        result_dic = result_array[0]
        return result_dic


# check if message is callback
def is_callback (dict):
    if 'callback_query' in dict:
        return True


# identify user number in config file
def check_user(userchatid):
    
    with open("config.json", "r") as jsonFile:
        config_data = json.load(jsonFile)
    position = 0

    for i in (config_data['Subscriber']):
        if (userchatid == i['id']):
            return position
        else:
            position = position + 1

    newSubscriber = {
            "id": userchatid,
            "alert_on": False,
            "interval": 600,
            "last_photo": 0
            }

    config_data['Subscriber'].append(newSubscriber)
    with open("config.json", "w") as jsonFile:
        json.dump(config_data, jsonFile, indent=2)        
    return position


# turn on/off alert
def toggle_alert(command, userchatid):
    with open("config.json", "r+") as jsonFile:
        config_data = json.load(jsonFile)      
    user_nr = check_user(userchatid)
    config_data['Subscriber'][user_nr]['alert_on'] = command
    with open("config.json", "w") as jsonFile:
        json.dump(config_data, jsonFile, indent=2)


# return status of alert 
def status_alert(userchatid):
    user_nr = check_user(userchatid)
    with open("config.json", "r") as jsonFile:
        config_data = json.load(jsonFile)
    alert_on = config_data['Subscriber'][user_nr]['alert_on']
    return alert_on



# sends text message
def send_message (chatId, message, print_response = True):
    data = {
        'chat_id': chatId,
        'text': message
        }
    response = requests.post(sendURL, json = data)  


# sends message with buttons
def send_message_button (chatId, message, buttonJSON):
    requests.post(sendURL + "?chat_id=" + str(chatId) + "&reply_markup=" + buttonJSON + "&text=" + message)


# send photo
def send_photo (chatId, numberOfRats, confidence):
    print("Trying to send photo to Telegram server...")
    img = {'photo': open(picpath,'rb')}

    
    if (numberOfRats == 1):
        caption_msg = str(numberOfRats) + " rat has been detected with a confidence of " + "{:.0%}".format(confidence[0])
    else:
        caption_msg = str(numberOfRats) + " rats have been detected with a confidence of " + "{:.0%}".format(confidence[0])
        i = 1
        while (i < numberOfRats-1):
            caption_msg += ", {:.0%}".format(confidence[i])
            i = i + 1
        caption_msg += " and {:.0%}".format(confidence[i])
     
    params = {'chat_id': chatId, 'caption': caption_msg}   
    requests.post(sendPhotoURL, params=params, files=img)


# change notification interval
def change_interval(userchatid, user_msg):

    send_message (userchatid, user_msg)
    intervalChanged = False

    while(intervalChanged == False ):
        newIntervalMessage = update(requestURL)
        if (newIntervalMessage):
            
            try:
                with open("config.json", "r") as jsonFile:
                    config_data = json.load(jsonFile)
                user_nr = check_user(userchatid)
                
                if (int(newIntervalMessage['message']['text']) >= 0):
                    config_data['Subscriber'][user_nr]['interval'] = int(newIntervalMessage['message']['text'])
                    with open("config.json", "w") as jsonFile:
                        json.dump(config_data, jsonFile, indent=2)
                    intervalChanged = True
                    user_msg = "Interval successfully updated"
                else:
                    user_msg = "Invalid input"
            
            except:
                user_msg = "Invalid input"
            
            send_message (userchatid, user_msg)

        time.sleep(0.5)


# handling of input messages
def handler_user_input():

    newmessage = update (requestURL)      
    try:
        if newmessage != False:
            if is_callback(newmessage) == True:
                userchatid = newmessage['callback_query']['message']['chat']['id']
                username = newmessage['callback_query']['message']['chat']['first_name']
                callback_data = newmessage['callback_query']['data']
                
                if callback_data == "IntervalButton":
                    user_msg = "Please insert an interger as new notification interval in seconds. " + \
                        "This limits the amount of notifications. A new notification is sent " + \
                        "if the interval is expired or the number of rats has been changed."
                    change_interval(userchatid, user_msg)
                elif callback_data == "TurnOffKnopf":
                    toggle_alert(False, userchatid)
                elif callback_data == "TurnOnKnopf":
                    toggle_alert(True, userchatid)
    
            else:
                userchatid = newmessage['message']['chat']['id']
                username = newmessage['message']['chat']['first_name']
                if (status_alert(userchatid)):
                    buttonDict11 = {"text":"Turn off notifications", "callback_data":"TurnOffKnopf"}
                else:
                    buttonDict11 = {"text":"Turn on notifications", "callback_data":"TurnOnKnopf"}
                buttonDict12 = {"text":"Change notification interval", "callback_data":"IntervalButton"}
                buttonArr1 = {"inline_keyboard":[[buttonDict11], [buttonDict12]]}
                send_message_button (userchatid, "Hi " + username + ", please choose a setting", json.dumps(buttonArr1))            

    except Exception as e:
        print ("Error:", e)

####################
# END TELEGRAM PART#file
####################

"""
Assemble all the necessary data points and send them to the back-end
"""
def sendImageMetaData(encodedImageData, confidence, numberOfRats):
    imageMetaData = {
    "image": encodedImageData,
    # "timeStamp": timeStamp,       Discuss if timestamp should be provided by front- or back-end
    "confidence": confidence,
    "numberOfRats": numberOfRats
    }

    imageMetaDataJSON = json.dumps(imageMetaData)

    headers = {'Content-type': 'application/json'}
    print("Trying to send...")
    try:
        response = requests.post("http://192.168.188.26:30500/api/detections", headers=headers, data=imageMetaDataJSON)
    
        if(response.status_code == 201):
            print('Success')
        else:
            print(response)
    except ConnectionError as e:    
        print(e)


def main():  

    model = torch.hub.load('ultralytics/yolov5', 'custom', 'weights/best.pt', force_reload=True)
    model.conf = 0.7

    sendIntervallCluster = 30
    lastPicSend = time.time() - sendIntervallCluster

    while True:
        try:
            time.sleep(2)
            print('-----------------------------------------------------')
            img = "picture.jpg"
            results = model(img)

            print(results.pandas().xyxy[0])

            numberOfRats = 0
            confidence = []

            pred = results.pandas().xyxy[0]

            for index, row in pred.iterrows():
                if row['confidence'] > model.conf:
                    numberOfRats += 1
                    confidence.append(row['confidence'])

            confidence_str = ''
            for el in confidence:
                el = el * 100
                confidence_str += '{:.2f}'.format(round(el, 2)) + ','


            print("Number of rats detected: " + str(numberOfRats))
            print("Confidence: " + str(confidence))

            results.ims  # array of original images (as np array) passed to model for inference
            results.render()  # updates results.ims with boxes and labels         

            handler_user_input() #checks for Telegram input
                                
            if numberOfRats > 0:           
                for im in results.ims:
                    buffered = BytesIO()
                    im_base64 = Image.fromarray(im)
                    im_base64.save(buffered, format="JPEG")
                    encodedImg = base64.b64encode(buffered.getvalue()).decode('utf-8')
                    img_to_save = Image.open(BytesIO(base64.decodebytes(bytes(encodedImg, 'utf-8'))))
                    img_to_save.save('detect.jpg')

                    # send to cluster

                    if ( lastPicSend + sendIntervallCluster < time.time()):
                        print(confidence_str[:-1])
                        sendImageMetaData(encodedImageData=encodedImg, confidence=confidence_str[:-1], numberOfRats=numberOfRats)
                        lastPicSend = time.time()

                    # sends to Telegram bot
                    
                    with open("config.json", "r") as jsonFile:
                        config_data = json.load(jsonFile)                    
                    for i in (config_data['Subscriber']):
                        if (i['alert_on'] == True and (i['last_photo'] + i['interval']) < time.time()):
                            userchatid = i['id']
                            send_photo (userchatid, numberOfRats, confidence)
                            user_nr = check_user(userchatid)
                            config_data['Subscriber'][user_nr]['last_photo'] = time.time()
                            with open("config.json", "w") as jsonFile:
                                json.dump(config_data, jsonFile, indent=2)

            # timeStamp = 
        except IOError as e:    
            print('Race Condition occured')


if __name__ == "__main__":
    main() 