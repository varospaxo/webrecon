import socket
import os
import subprocess
print("\n-----------Reverse DNS Scanner Started-----------\n")
try:
  with open('./Temp/Result_current.txt') as f:
      hostname = f.readline().strip()
      currenttime = f.readline().strip()
      hostip = f.readline().strip()
      
      print ("Domain Name: "+hostname)
      print ("IP Address: "+hostip)
      f = open("./ReverseDNS.txt", "a")
      f.write ("Domain Name: "+hostname)
      f.write ("\nIP Address: "+hostip)
      f.close()

  def get_domain_name(ip_address):
    result=socket.gethostbyaddr(ip_address)
    return list(result)[0]
  # print("Domain name using PTR DNS:")
  print("Reverse DNS address: "+get_domain_name(hostip))
  f = open("./ReverseDNS.txt", "a")
  f.write ("\nReverse DNS address: "+get_domain_name(hostip))
  f.close()
except socket.herror:
  print("\nCould not find results for reverse DNS search!!!")
  f = open("./ReverseDNS.txt", "a")
  f.write ("\nCould not find results for reverse DNS search!!!")
  f.close()
  
#Remove Temp File Save Output File
path_current="./ReverseDNS.txt"
movepath = "./Temp/ReverseDNS_OP.txt" 
os.replace(path_current, movepath)
print("\n-----Scanning Finished-----")

#Run Next Script
rawpath = os.getcwd() + "\\SubdomainRoutes.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])
