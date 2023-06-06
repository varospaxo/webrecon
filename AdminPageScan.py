#!/usr/bin/python3

from threading import Lock, Thread
from requests import get
import os
import subprocess
from queue import Queue
from time import sleep

print("\n\n---------Admin Page Scanner Started---------\n")
file = open("./AdminPages.txt", "a")          
file.writelines("")
file.close()
proxy_enable = False
delay = 0.2
file_to_open = './Lists/AdminPageList.txt'
with open("./Temp/Result_current.txt") as f:
    websites_to_scan = "https://"+str(f.readline().strip())
    print("Detecting Admin Pages of: "+websites_to_scan)

# used threading things #
# Lock
# Thread
print_lock = Lock()
q = Queue()
# run thread function using Queue and Thread()
def thread(website):
    worker = q.get()
    try:
        if not proxy_enable:
            r = get('{}{}'.format(website, worker))

        if r.ok:
            result = "[Status-code - "+'{}'.format(r.status_code)+"] Success: "+ worker 
            # result = ('    [Status-code - {}] Success: '.format(r.status_code), worker)
            print(result)
            file = open("./AdminPages.txt", "a")          
            file.writelines(result)
            file.writelines("\n")
            file.close()

    except:
        print ('Connection Error')
        file = open("./AdminPages.txt", "a")          
        file.writelines('Connection Error')
        file.writelines("\n")
        file.close()

if type(websites_to_scan) is str:
    websites_to_scan = [websites_to_scan]

for website in websites_to_scan:
    if website[-1] != '/':
        website = website + '/'
    # put admin panel urls to queue
    with open(file_to_open, 'r') as f:
        for line in f:
            q.put(line.strip().encode().decode('utf-8'))
    # create thread and run till Queue is empty
    print ('Result for {}:'.format(website))
    while not q.empty():
        t = Thread(target=thread, args=(website,), daemon=True)
        t.start()
        sleep(delay)
    t.join()

path_current="./AdminPages.txt"
movepath = "./Temp/AdminPages_OP.txt"
os.replace(path_current, movepath)
print('\n----Scanning Finished----')
print('-----Scanner Stopped-----\n')
#Run Next Script
rawpath = os.getcwd() + "\\Reporter.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])

