#!/usr/bin/env python3

import os
from datetime import datetime
import sys
import emails 
import reports

path = "/home/student-01-3060a68708a8/supplier-data/descriptions"

def main(argv):
  months = {
            1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May",
            6 : "June", 7 : "July", 8 : "August", 9 : "September",
            10 : "October", 11 : "November", 12 : "December" 
           }
  data = []
  for file in os.listdir(path):
    if not file.endswith('.txt'):
        continue
    lines = open(path+"/"+file).readlines()
    data.append("name: {}<br/>weight: {}<br/>".format(lines[0].strip('\n'),lines[1].strip('\n')))
  date = datetime.today()
  print(data)
  reports.generate("/tmp/processed.pdf","Processed Update on {} {}, {}".format(months[date.month],date.day,date.year),"<br/>".join(data))
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
