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

def timed_block(time_from, time_until):
    while True:
      
        # time of your work 
        if dt(dt.now().year, dt.now().month, dt.now().day,time_from) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,time_until):
            print("Working hours...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n") 
        else: 
            with open(hosts_path, 'r+') as file: 
                content=file.readlines() 
                file.seek(0) 
                for line in content: 
                    if not any(website in line for website in website_list): 
                        file.write(line) 
      
                # removing hostnames from host file 
                file.truncate() 
      
            print("Fun hours...") 
        time.sleep(5)

def block():
    with open(hosts_path, 'r+') as f:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + '\n')

def enable():
    with open(hosts_path, 'r+') as file: 
        content=file.readlines() 
        file.seek(0) 
        for line in content: 
            if not any(website in line for website in website_list): 
                file.write(line)
  
        # removing hostnames from host file 
        file.truncate()

parser = argparse.ArgumentParser(description='Tool to block youtube')
parser.add_argument('-t', '--timed', nargs=2, help='Sets a timed block on youtube')
group = parser.add_mutually_exclusive_group()
group.add_argument('-b', '--block', action='store_true', help='block for the time being')
group.add_argument('-e', '--enable', action='store_true', help='enable youtube again')

if(args.timed is not None):
    timed_block(args.timed[0],args.timed[1])
elif(args.block):
    block()
elif(args.enable):
    enable()
else:
    print("Please enter an argument for the program to run properly")
