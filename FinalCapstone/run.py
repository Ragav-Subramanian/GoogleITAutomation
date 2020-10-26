#! /usr/bin/env python3

import os
import requests

path = "/home/student-01-3060a68708a8/supplier-data/descriptions"

for file in os.listdir(path):
    if not file.endswith('.txt'):
        continue
    datadict = {}
    lines=open(path+"/"+file).readlines()
    datadict['name'] = lines[0].strip('\n')
    datadict['weight'] = int(lines[1].strip('\n').split()[0])
    datadict['description'] = lines[2].strip('\n')
    datadict["image_name"] = file.split('.')[0]+".jpeg"
    print(datadict)
    response = requests.post("http://34.66.178.211/fruits/",data=datadict,json=datadict)
    print(response.status_code,response.ok)
