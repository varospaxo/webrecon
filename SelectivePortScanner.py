import socket
import threading
import os
import subprocess

print("\n-----------Remote Port Scanner Started-----------")

def scan_ports(hostname, port_mappings):
    open_ports = []
    lock = threading.Lock()

    def scan_port(port, service):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            result = sock.connect_ex((hostname, port))
            if result == 0:
                with lock:
                    open_ports.append((port, service))
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {str(e)}")

    threads = []
    for port, service in port_mappings.items():
        thread = threading.Thread(target=scan_port, args=(port, service))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

def load_port_mappings(file_path):
    port_mappings = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    port, service = int(parts[0]), parts[1]
                    port_mappings[port] = service
        return port_mappings
    except FileNotFoundError:
        print(f"Port mapping file not found: {file_path}")
        return {}

def main():
    try:
        with open('./Temp/Result_current.txt') as f:
            hostname = f.readline().strip()
    except FileNotFoundError:
        print("Result_current.txt not found.")
        return

    try:
        ip = socket.gethostbyname(hostname)
        print(f"Scanning {hostname} ({ip}) for open ports...")
    except socket.gaierror:
        print("Invalid hostname or IP address.")
        return

    port_mappings = load_port_mappings("./Lists/port_mappings.txt")
    open_ports = scan_ports(ip, port_mappings)

    if open_ports:
        print("Open ports:")
        with open("./PortScannerFast.txt", "a") as file:
            for port, service in open_ports:
                print(f"Port {port} ({service}) is open.")
                file.write(f"Port {port} ({service}) is open.\n")
    else:
        print("No open ports found.")
        with open("./PortScannerFast.txt", "a") as file:
            file.write("No open ports found.\n")

if __name__ == "__main__":
    main()

path_current = "./PortScannerFast.txt"
movepath = "./Temp/PortScannerFast_OP.txt"
try:
    os.replace(path_current, movepath)
except FileNotFoundError:
    print(f"Error moving the result file: {path_current} not found.")

print("\n----Scanning Finished----\n")

rawpath = os.path.join(os.getcwd(), "Traceroute.py")
path = rawpath.replace('\\', '/')  # Convert backslashes to forward slashes for cross-platform compatibility

# Execute the subprocess (Python script)
subprocess.call(['python', path])
