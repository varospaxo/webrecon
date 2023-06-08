import time
import os
import subprocess
import shutil
import re

print ("Installing required packages...\n")
print ("Please Wait...\n")
if os.system('pip install -r requirements.txt') == 0:
    os.system("cls")
else:
    print(f"\n-----------------------------------------\n")
    print(colored("Requirements not properly installed!!!", 'red'))
    print(colored("The script may generate improper results.", 'red'))

from termcolor import colored

if os.path.exists("Temp"):
  shutil.rmtree("Temp", ignore_errors=True)
else:
    pass

print("")
print(colored(" _       __     __    ____                      ", 'cyan', attrs=["bold"]))
print(colored("| |     / /__  / /_  / __ \___  _________  ____", 'cyan', attrs=["bold"])) 
print(colored("| | /| / / _ \/ __ \/ /_/ / _ \/ ___/ __ \/ __ \\", 'cyan', attrs=["bold"]))
print(colored("| |/ |/ /  __/ /_/ / _, _/  __/ /__/ /_/ / / / /", 'cyan', attrs=["bold"]))
print(colored("|__/|__/\___/_.___/_/ |_|\___/\___/\____/_/ /_/ ", 'cyan', attrs=["bold"]))

print(colored('By - ','green')+colored("varospaxo", 'red')+colored('                            v2.0','green'))
print("\n")
hostname = input("Enter the hostname: ")
def isValidDomain(str):
 
    # Regex to check valid
    # domain name.
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" +"+[A-Za-z]{2,6}"
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

while isValidDomain(hostname) == False:
    print("Invalid domain name format!!!\n")
    hostname = input("Re-enter the hostname: ")
else:
    file = open("./Result.txt", "a")         
    file.write(hostname)
    t = time.localtime()
    current_time = time.strftime("%m-%d-%Y_%H:%M:%S", t)
    file.write ("\n"+str(current_time))
    print("Current Time: ",current_time)
    file.close()

if os.path.exists("Temp"):
    shutil.rmtree("Temp", ignore_errors=True)
else:
    os.mkdir("Temp")
    
if os.path.exists("OutputFiles"):
    pass
else:
    os.mkdir("OutputFiles")

path_current="./Temp/Result_current.txt"
os.replace("./Result.txt", path_current)
rawpath = os.getcwd() + "\\Ping.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
