# isolated program for testing my host_up function
from os import system
import socket

def host_up(full_addr: str):
    check_ping = False # assumes that host will not respond to pings
    if system("ping -c 1 " + full_addr) == 0: # if host responds when pinged
        print("Host is up")
        return True

#host_up("192.168.1.123")

from nmap import PortScanner
from socket import gethostbyname
def host_up2(full_addr):
    scanner = PortScanner()
    host = gethostbyname(full_addr)
    scanner.scan(host, '1', '-v')
    print("IP Status: ", scanner[host].state())

# host_up2("192.168.1.199")

def host_up3(full_addr: str): # function to determine if a host is up
    # checks if host can be pinged
    # pass
    # if system("ping -c 1 " + full_addr) == 0: # if host responds when pinged
    #     print("Host is up")
    #     return True
    # else: # ping failed, either host is down or has blocked pings
        # try on http port
    port = 51243
    print(type(full_addr))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)   
    # returns an error indicator
    result = s.connect_ex((full_addr,port))
    print(result, "brug")
    if result == None:
        print("Port closed")
    elif result != 61:
        print(f"Port {port} is open")
    s.close()
    return True
#return False

host_up3("192.168.1.120")