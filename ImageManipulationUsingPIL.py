#!/usr/bin/env python3

from PIL import Image
import os 

pathdir = "/home/student-03-2a3df5d7d453/"

for image in os.listdir(pathdir+"images"):
    try:
        img = Image.open(pathdir+"images"+"/"+image).rotate(90).resize((128,128))
        print(img.format,img.size)
        ii = img.convert('RGB').save(pathdir+"UpdatedImages/"+image,'JPEG')
        print("DONE")
    except:
        print("Exception")
