#!/usr/bin/env python3

from urllib.request import urlopen
import json
import sys


ip = sys.argv[1]

url = "http://"+ip+"/data.json"
response = urlopen(url)
data_json = json.loads(response.read())

print(data_json['sensordatavalues'][0]['value'])

