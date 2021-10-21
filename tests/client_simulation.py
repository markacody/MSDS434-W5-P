"""
Two functions simulate client requests against the API.
Requires a running server.

make start-api

"""

import requests
import json
import base64

# Failed query parameters simulation
url = 'http://0.0.0.0:5001/api/aggregate'
with open('..ext/input.csv', 'rb') as f:
    data = base64.b64encode(f.read())

# Not enough parameters
payload = {'column': 'count'}
headers = {'Content-Type': 'application/json'}
r = requests.put(url, data=data, params=payload, headers=headers)
print('Status code: ', r.status_code)
print('Response body: ', json.loads(r.content))

# Successful query parameters simulation
url = 'http://0.0.0.0:5001/api/aggregate'
with open('..ext/input.csv', 'rb') as f:
    data = base64.b64encode(f.read())

payload = {'column': 'count', 'groupby': 'last_name'}
headers = {'Content-Type': 'application/json'}
r = requests.put(url, data=data, params=payload, headers=headers)
print('Status code: ', r.status_code)
print('Response body: ', json.loads(r.content))
