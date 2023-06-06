import time
import os
import subprocess
print("")
print(" _       __     __    ____                      ")
print("| |     / /__  / /_  / __ \___  _________  ____") 
print("| | /| / / _ \/ __ \/ /_/ / _ \/ ___/ __ \/ __ \\")
print("| |/ |/ /  __/ /_/ / _, _/  __/ /__/ /_/ / / / /")
print("|__/|__/\___/_.___/_/ |_|\___/\___/\____/_/ /_/ ")
print("                                                ")
hostname = input("Enter the hostname: ")
file = open("./Result.txt", "a")         
file.write(hostname)
t = time.localtime()
current_time = time.strftime("%m-%d-%Y_%H:%M:%S", t)
file.write ("\n"+str(current_time))
print("Current Time: ",current_time)
file.close()
if os.path.exists("Temp"):
    pass
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
