import requests
import json

wh_url = 'http://127.0.0.1:5000/webhook'

data = {'email' : 'daftpunkapi@gmail.com',
        'key' : '38nMKRsJFK2CGA57Dr3F7539',
        'sub' : 'dpapi55'}

r = requests.post(wh_url, data = json.dumps(data), headers = {'Content-Type' : 'application/json'})

print(r.text)