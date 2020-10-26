#!/usr/bin/env python3

import psutil 
import emails

def report_it(subject_line):
  sender = "automation@example.com"
  receiver = "{}@example.com".format("student-00-1f8a9ce3b2b1")
  subject = subject_line
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_error_report(sender, receiver, subject, body)
  emails.send(message)

percentage = psutil.cpu_percent(59)
print(percentage)
try:
  if percentage > 80.0:
    report_it("Error - CPU usage is over 80%")
except:
  report_it("Error - localhost cannot be resolved to 127.0.0.1")
disk_used = psutil.disk_usage('/').percent
print(disk_used)
if disk_used < 20.0:
  report_it("Error - Available disk space is less than 20%")
memory = (psutil.virtual_memory().available/1024)/1024
print(memory)
if memory<500.0:
  report_it("Error - Available memory is less than 500MB")

