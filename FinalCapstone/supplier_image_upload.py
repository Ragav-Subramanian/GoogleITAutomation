#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

pathdir = "/home/student-01-3060a68708a8/supplier-data/images"


for image in os.listdir(pathdir):
  if not image.endswith(".jpeg"):
    continue
  with open(pathdir+"/"+image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
