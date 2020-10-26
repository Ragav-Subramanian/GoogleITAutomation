#!/usr/bin/env python3

from PIL import Image
import os 

pathdir = "/home/student-01-3060a68708a8/supplier-data/images"

for image in os.listdir(pathdir):
    try:
        img = Image.open(pathdir+"/"+image)
        image=image.split(".")[0]
        img.convert('RGB').resize((600,400)).save(pathdir+"/"+image+".jpeg",'JPEG')
        print(img.format,img.size,img.filename)
    except:
        print("Exception")
