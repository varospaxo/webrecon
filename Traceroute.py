import sys
import scapy.all as scapy
import os
import subprocess

try:
    print("\n-----------Traceroute Scan Started-----------\n")
    
    with open('./Temp/Result_current.txt') as f:
        hostname = f.readline().strip()
        currenttime = f.readline().strip()
        target = f.readline().strip()
        print(target)
    
    if len(sys.argv) == 2:
        target = sys.argv[1]

    ans, unans = scapy.sr(scapy.IP(dst=target, ttl=(1, 22), id=scapy.RandShort()) / scapy.TCP(flags=0x2), timeout=10)

    for snd, rcv in ans:
        if isinstance(rcv.payload, scapy.TCP):
            rambo = "(TCP)"
        else:
            rambo = ""
        print(snd.ttl, rcv.src, rambo)
        f = open("./Traceroute.txt", "a")
        f.writelines(str(snd.ttl) + "." + " " + str(rcv.src) + " " + rambo)
        f.writelines("\n")
        f.close()
    
    path_current = "./Traceroute.txt"
    movepath = "./Temp/Traceroute_OP.txt"
    os.replace(path_current, movepath)

    print("\n-----Scanning Finished-----\n")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    # Run Next Script
rawpath = os.getcwd() + "/OSDetect.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])


