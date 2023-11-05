from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor
import os
import subprocess

print("\n-----------Remote Port Scanner Started-----------")

# returns True if a connection can be made, False otherwise
def test_port_number(host, port):
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(4)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((host, port))
            # a successful connection was made
            return True
        except:
            # ignore the failure
            return False

# scan port numbers on a host
MAX_CONCURRENT_PORTS = 100  # Adjust this value as needed

def port_scan(host, ports):
    print(f'\nPort Scanning {host}...')
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_PORTS) as executor:
        results = executor.map(test_port_number, [host] * len(ports), ports)
        for port, is_open in zip(ports, results):
            if is_open:
                print(f'> {host}:{port} open')
                with open("./PortScannerFast.txt", "a") as file:
                    file.write("[+] " + str(port) + "\n")

# Define host and port numbers to scan
with open('./Temp/Result_current.txt') as f:
    hostname = f.readline().strip()
HOST = hostname
PORTS = range(4096)

# Test the ports
port_scan(HOST, PORTS)

path_current = "./PortScannerFast.txt"
movepath = "./Temp/PortScannerFast_OP.txt"
os.replace(path_current, movepath)
print("\n----Scanning Finished----\n")

rawpath = os.path.join(os.getcwd(), "Traceroute.py")
path = rawpath.replace('\\', '/')  # Convert backslashes to forward slashes for cross-platform compatibility

# Execute the subprocess (Python script)
subprocess.call(['python', path])
