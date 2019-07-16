# Run this script as root 
  
import time
from datetime import datetime as dt
import argparse
 
# hosts path
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"
  
# websites That you want to block 
website_list = ["www.youtube.com","youtube.com"]

with open(hosts_path, 'r+') as file: 
    content=file.readlines() 
    file.seek(0) 
    for line in content: 
        if not any(website in line for website in website_list): 
            file.write(line)

    # removing hostnames from host file 
    file.truncate()
