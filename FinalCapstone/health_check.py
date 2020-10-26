#!/usr/bin/env python3

import shutil
import psutil 
import emails

disk_used = psutil.disk_usage('/').percent
print(disk_used)
memory = (psutil.virtual_memory().available/1024)/1024
print(memory)
