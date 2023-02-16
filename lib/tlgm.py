import requests, json, time


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
    g_base_url = "https://api.telegram.org/bot"

    def __init__(self, token, chat_id):
        self.chat_id = chat_id
        self.token = token
        self.base_url = self.g_base_url + self.token + '/'

    def sendTxt(self, msg):
        self.base_url += 'sendMessage'
        parameters = {'chat_id': self.chat_id, 'text': msg}
        r = requests.get(url = self.base_url, params=parameters)
        return json.loads(json.dumps(r.json()))

    def sendMessage(self, text):
        if self.chat_id:
            if text == '':
                return "Message can't be emply !"  
            responce_data = self.sendTxt(text)
            if responce_data['ok']:
                return 'Messages Send Succesfully!'
            else:
                return 'There is problem with the data you can check by check the respoce data %s' % responce_data 
        else:
            return "Please provide the chat_id!"
            
    def send_current_time(self):
        text = time.strftime("%H:%M:%S", time.localtime())
        responce_data = self.sendTxt(text)
        if responce_data['ok']:
            return 'Messages Send Succesfully! with current time - ' + text
        else:
            return 'There is problem with the data you can check by check the respoce data %s' % responce_data 
