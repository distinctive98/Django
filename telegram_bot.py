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
