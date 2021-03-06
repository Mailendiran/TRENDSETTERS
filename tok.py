import requests
TOKEN = "702271639:AAHttXpYn4RSAsDpa91yiZEtvruBqdxzvAc"
import requests
import time    
import urllib
import os
from flask import Flask,redirect, url_for,request,render_template
from threading import Thread

app = Flask(__name__)

URL = "https://api.telegram.org/bot{}/".format(TOKEN)
print('Started')

@app.route('/')
def main():
    return f'''Cool'''

from datetime import *
def restart():
    while True:
        try:
            v=(datetime.utcnow()+timedelta(hours=5,minutes=30))
            if(5*60<v.hour*60+v.minute<21*60+30):
                requests.head('http://trendsettersbot.herokuapp.com/up/pys',timeout=25)
            sleep(25*60)
        except Exception as e:
            exception(e)
            sleep(60)
            continue


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    return  requests.get(url).json()

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url=URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    try:
        r=requests.get(url,timeout=30)
        if r.reason!='OK':print(r.text)
    except Exception as e:
        print(e)
        print(url)

def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)           
            z=updates.get("result")
            if z and len(z) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)
            time.sleep(0.5)
        except Exception as e:
            print(e)        


def echo_all(updates):
    for update in updates["result"]:
        try:
            print(update)
            chat = update["message"]["chat"]["id"]
            a = update["message"].get("text")
            #customize here
            if a: print(chat,a)
            send_message(a,chat)
        except Exception as e:
            print(e)

def snt(f,a,b=None):
  try:
    Thread(None,f,None,a,b).start()
  except Exception as e:
    return str(e)

snt(main,())
snt(restart,())


