# Run As Admin
import nmap
import socket
import os
import subprocess
print('\n-----------Remote OS Detection Started-----------\n')
try:
    try:
        with open('./Temp/Result_current.txt') as f:
            hostname = f.readline().strip()
            print("Detecting Host Operating System for: "+hostname)
        hostip = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        machine = nm.scan(hostip, arguments='-O')
        print("OS Type: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['osfamily'])
        print("Detection Accuracy: ", machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['accuracy'])

        f = open("./OSDetect.txt", "a")
        f.write("OS Type: "+machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['osfamily']+"\n")
        f.write("Detection Accuracy: "+machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['accuracy'])
        f.close()
        
    except IndexError:
        print("Cannot Detect OS for: "+hostname)
        f = open("./OSDetect.txt", "a")
        f.write("Cannot Detect OS for: "+hostname)
        f.close()
        
    path_current="./OSDetect.txt"
    movepath = "./Temp/OSDetect_OP.txt" 
    os.replace(path_current, movepath)
    rawpath = os.getcwd() + "\\SSLCertificate.py"
    path = rawpath.replace('\\', '/')
    subprocess.call(['python', path])
except:
    rawpath = os.getcwd() + "\\SSLCertificate.py"
    path = rawpath.replace('\\', '/')
    subprocess.call(['python', path])
