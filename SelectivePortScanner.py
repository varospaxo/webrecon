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
        except Exception:
            pass

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
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                port, service = int(parts[0]), parts[1]
                port_mappings[port] = service
    return port_mappings

def main():
    with open('./Temp/Result_current.txt') as f:
        hostname = f.readline().strip()
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Scanning {hostname} ({ip}) for open ports...")
    except socket.gaierror:
        print("Invalid hostname or IP address.")
        return

    port_mappings = load_port_mappings("./Lists/AdminPageList.txt")
    open_ports = scan_ports(ip, port_mappings)

    if open_ports:
        print("Open ports:")
        for port, service in open_ports:
            print(f"Port {port} ({service}) is open.")
            with open("./PortScannerFast.txt", "a") as file:
                    file.write(f"Port {port} ({service}) is open." + "\n")
    else:
        print("No open ports found.")
        with open("./PortScannerFast.txt", "a") as file:
                    file.write("No open ports found.")

if __name__ == "__main__":
    main()

path_current = "./PortScannerFast.txt"
movepath = "./Temp/PortScannerFast_OP.txt"
os.replace(path_current, movepath)
print("\n----Scanning Finished----\n")

rawpath = os.path.join(os.getcwd(), "Traceroute.py")
path = rawpath.replace('\\', '/')  # Convert backslashes to forward slashes for cross-platform compatibility

# Execute the subprocess (Python script)
subprocess.call(['python', path])
