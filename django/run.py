#! /usr/bin/env python3

import os
import requests

path = '/data/feedback'

for file in os.listdir(path):
    if not file.endswith('.txt'):
        continue
    datadict = {}
    lines=open(path+"/"+file).readlines()
    datadict['title'] = lines[0].strip('\n')
    datadict['name'] = lines[1].strip('\n')
    datadict['date'] = lines[2].strip('\n')
    datadict['feedback'] = lines[3].strip('\n')
    response = requests.post("http://34.66.32.49/feedback/",data=datadict,json=datadict)
    print(response.status_code,response.ok)
