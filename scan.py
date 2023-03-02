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


targets = input("[*]Enter Targets to scan(split them by ,):")
ports = int(input("[*] Enter How many ports you want to scan: "))
if ',' in targets:
    print("[*]Scan multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else: 
      scan(targets, ports) 