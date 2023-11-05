from pythonping import ping
import socket
import os
import subprocess

hostname = ""
print("\n-----------Host Service Detection-----------\n")
try:
    with open('./Temp/Result_current.txt') as f:
        hostname = f.readline()
        print ("Host status for: "+ hostname)
        ip_address = socket.gethostbyname(hostname.strip())
        file = open("./Temp/Result_current.txt", "a")          
        file.write("\n"+ip_address)
        file.close()
        file = open("./Ping.txt", "a")          
        file.write("IP Address: "+ip_address)
        file.close()
    print("IP Address: ", ip_address)
    response_list = ping(ip_address, size=40, count=10)
    if response_list.rtt_avg_ms > 0:
        print ("Host is UP!")
        file = open("./Ping.txt", "a")          
        file.write("\nHost is UP!")
        file.close()
    else:
        print("Host is DOWN!")
        file = open("./Ping.txt", "a")          
        file.write("\nHost is DOWN!")
        file.close()
    print("Ping Avg Response Time:", response_list.rtt_avg_ms)
    file = open("./Ping.txt", "a")          
    file.write("\nPing Avg Response Time: "+str(response_list.rtt_avg_ms))
    file.close()
except socket.gaierror:
    print("Hostname unavailable!")
    file = open("./Ping.txt", "a")          
    file.write("Hostname unavailable!")
    file.close()
    exit()
path_current="./Ping.txt"
movepath = "./Temp/Ping_OP.txt" 
os.replace(path_current, movepath)
print("\n----Scanning Finished----\n")
rawpath = os.getcwd() + "\\SelectivePortScanner.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])

