#!/usr/bin/python3
import requests

headers = {'DD-API-KEY': '9a9aab4f0b5058eea4df95027b39dbf9',
           'DD-APPLICATION-KEY': 'bbfbd3d76f3ae56c35e431c2e7c1ca090d30853c'}

req = requests.get('https://api.datadoghq.com/api/v1/dashboard', headers=headers)

data_json = req.json()

print(data_json)
