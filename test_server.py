from flask import Flask, request, abort
import pandas as pd
import requests
import json
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        x = request.json
        # x = json.loads(x)
        username = x["email"]
        password = x["key"]
        subdomain = x["sub"]
        
        print(username,password,subdomain)
        del x
        return 'success', 200
        
    else:
        abort(400)

if __name__ == '__main__':
    app.run()