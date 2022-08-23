#!/usr/bin/env python3

from urllib.request import urlopen
import json
import sys


ip = sys.argv[1]
change = sys.argv[2]

url = "http://"+ip+"/data.json"
response = urlopen(url)
data_json = json.loads(response.read())
pm10 = data_json['sensordatavalues'][0]['value']
pm2 = data_json['sensordatavalues'][1]['value']

if change == '2':
    print(pm2)
elif change == '10':
    print(pm10)


