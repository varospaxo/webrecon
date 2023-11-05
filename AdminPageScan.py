from threading import Lock, Thread
from requests import get
import os
import subprocess
from queue import Queue
from time import sleep

print("\n\n---------Admin Page Scanner Started---------\n")

# Create AdminPages.txt file
with open("./AdminPages.txt", "w") as file:
    file.write("")

proxy_enable = False
delay = 0.2
file_to_open = './Lists/AdminPageList.txt'

with open("./Temp/Result_current.txt") as f:
    websites_to_scan = ["https://" + f.readline().strip()]
    print("Detecting Admin Pages of: " + websites_to_scan[0])

# Lock and Queue for threading
print_lock = Lock()
q = Queue()

# Thread function
def thread(website):
    while not q.empty():
        worker = q.get()
        try:
            if not proxy_enable:
                url = '{}{}'.format(website, worker)
                r = get(url)

                if r.status_code == 200:
                    result = "[Status-code - {}] Success: {}".format(r.status_code, worker)
                    with print_lock:
                        print(result)
                    with open("./AdminPages.txt", "a") as file:
                        file.write(result + "\n")
            else:
                with print_lock:
                    print('Proxy is enabled, please configure proxy settings.')
        except Exception as e:
            with print_lock:
                print('Connection Error: {}'.format(e))

# Prepare websites to scan
if websites_to_scan and websites_to_scan[0][-1] != '/':
    websites_to_scan[0] = websites_to_scan[0] + '/'

# Put admin panel URLs to the queue
with open(file_to_open, 'r') as f:
    for line in f:
        q.put(line.strip())

# Create threads and run until the queue is empty
for website in websites_to_scan:
    print('Result for {}:'.format(website))
    threads = []

    for _ in range(5):  # Adjust the number of threads as needed
        t = Thread(target=thread, args=(website,), daemon=True)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

path_current = "./AdminPages.txt"
movepath = "./Temp/AdminPages_OP.txt"
os.replace(path_current, movepath)
print('\n----Scanning Finished----')
print('-----Scanner Stopped-----\n')

# Run the next script
rawpath = os.path.join(os.getcwd(), "Reporter.py")
path = rawpath.replace(os.path.sep, '/')
subprocess.call(['python', path])
