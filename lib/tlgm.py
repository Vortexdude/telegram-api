import requests, json


# .  Created by - Nitin Namdev
# .  Aim - to send and recieve message using telegram
# .  impliment - use can use as the ansible module to send and recieve alerts of the server
# .  focus - will be impliment other telegram methods
# .  Thank you for using 
# . You can reach me at - itsmyidbro@gmail.com


# Abjective - To sends and recieve the telegame messages using the telegram api
# Usage - : 
# 1. Import the class by these
# > from tlgm import telegram

# 2. create an object with the telegram class and pass the chat_id and token like this 
# > app = telegram(token, chat_id)

# 3. call the sendMessage method with the message
# > responce = app.sendMessage(text='From the validation')
# > print(responce)



class telegram():

    def __init__(self, token, chat_id):
        self.chat_id = chat_id
        self.token = token

    def sendMessage(self, text):
        base_url = "https://api.telegram.org/bot"
        if self.chat_id:
            if text == '':
                return "Message can't be emply !"  
            parameters = {'chat_id': self.chat_id, 'text': text}
            full_url = f"{base_url}{self.token}/sendMessage"
            r = requests.get(url = full_url, params=parameters)
            responce_data =  json.loads(json.dumps(r.json()))
            status = responce_data['ok']
            if status:
                return 'Messages Send Succesfully!'
            else:
                return 'There is problem with the data you can check by check the respoce data %s' % responce_data 
        else:
            return "Please provide the chat_id!"
