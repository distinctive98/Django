from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pprint

app = Flask(__name__)

base = 'https://api.telegram.org'
token = config('TOKEN')

@app.route('/')
def write():
    return render_template('write.html')

@app.route(f'/{token}', methods=['POST'])
def webhook():
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서
    url = f'{base}/bot{token}/setWebhook?url='