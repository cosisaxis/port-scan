import socket

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
           s = socket.socket()
           s.connect((ipaddress, port))
           print("[+] Port Opened " + str(port))
           s.close()



    except:
        print("[-] Ports Closed " + str(port))


targets = input("")
ports = input("")
if ',' in targets:
    print("")
    scan(target, ports)