import ssl
import socket
import datetime
import boto3
import os
import subprocess

client = boto3.client("ses", region_name="us-east-1")

print(f"\n-----------SSL Status Service Started-----------\n")

# ##opening file
# host = input("Enter Hostname: ")
with open('./Temp/Result_current.txt') as f:
    host = f.readline().strip()
# port= input ("Enter Port (80, 8080, 443): ")
port='443'
try:
            print(f"Checking certifcate for server {host}")
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    certificate = ssock.getpeercert()
                certExpires = datetime.datetime.strptime(
                    certificate["notAfter"], "%b %d %H:%M:%S %Y %Z"
                )
                daysToExpiration = (certExpires - datetime.datetime.now()).days
                print(f"Expires on: {certExpires} in {daysToExpiration} days")
                f = open("./SSLCert.txt", "a")
                f.write(f"SSL Certificate expires on: {certExpires} in {daysToExpiration} days")
                f.close()
                
except:
            print(f"Error on connection to Server or incorrect port selected, {host}")
            f = open("./SSLCert.txt", "a")
            f.write("Error on connection to Server or incorrect port selected ")
            f.close()

#Remove Temp File Save Output File
path_current="./SSLCert.txt"
movepath = "./Temp/SSLCert_OP.txt" 
os.replace(path_current, movepath)

print(f"\n-----Scanning Finished-----\n")

#Run Next Script
rawpath = os.getcwd() + "\\ReverseDNS.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])