# Author’s name
# Email address 
# Copyright (as 'Copyright Red Opal Innovations')
# License (as 'Proprietary') 
# Last updated date
# Version (numbered starting 1.0.1)
# Status (set initially to 'development') 
# An overview of the script's logic

"""
Global variables: logs[]
"""

# Imports

from socket import inet_aton as valid_ipv4, gethostbyname, AF_INET, SOCK_STREAM, setdefaulttimeout, socket
import pyfiglet as ascii_text
from datetime import datetime
import syslog
from os import system

# Function for writing to log file
def log(payload):
    try:
        file = open("ip_port_log.txt", "a") # open log in append mode
        file.write(payload) # write the payload
        file.close() # close the file
    except Exception as error: # if an error occurs
        print(f"Error occured\n{error}") # print error

# Function for accepting a valid network IP address
def enter_ip():
    netw_addr = input(
        "Enter a valid class C network IP address with the first 3 octets "
            )
    # initial IP address validity check
    try:
        if valid_ipv4(f"{netw_addr}.1"): # if ip address is valid
            print("IP address passed first check") # ip address valid (broad)
    except OSError: # if ip address not valid
        print("IP address invalid, please re-enter") # ip address not valid
        enter_ip() # call the function to start again, this will repeat until a valid ip address is entered

    # secondary, more specific ip address check
    list_netw_addr = netw_addr.split(".") # splits each octet into a list variable
    list_netw_addr = [int(x) for x in list_netw_addr] # converts octets in list to strings
    octet_count = len(list_netw_addr) # gets the number of octets in the provided address
    print("Second IP address check in progress")
    if octet_count == 3: # check to make sure 3 octets have been provided
        # set each octet a more accessible variable name
        first_octet = list_netw_addr[0]; second_octet = list_netw_addr[1]; third_octet = list_netw_addr[2]
        # ensure the 3 octets have the correct ipv4 class C values
        if (
            223 >= first_octet >= 192 and
            second_octet == 168 and
            third_octet <= 255
        ):
            print("Provided IP address has the correct number of octets and the correct octet values") # ip address valid

            return calculate_range(f"{first_octet}.{second_octet}.{third_octet}") # calculate (and scan) the ip range and exit function
        
        print("IP address range not valid, try again") # notifies user
        enter_ip() # calls the function again
    # runs if wrong number of octets entered
    print("You haven't entered the correct number of octets, try again") # notifies user
    enter_ip() # calls the function again

def enter_subnet():
    subnet = input("Enter the subnet mask in extended form: ")
    subnet_list = subnet.split(".") # split each octet into a list element
    subnet_list = [int(x) for x in subnet_list] # convert octet elements to integers
    # define more accessible list variables
    first_octet = subnet_list[0]; second_octet = subnet_list[1]; third_octet = subnet_list[2]; fourth_octet = subnet_list[3]
    if (
        first_octet == 255 and
        second_octet == 255 and 
        third_octet == 255 and
        fourth_octet == 0
    ):
        return print("Valid subnet mask entered")
    print("Invalid subnet mask entered, please ensure you enter the class C subnet mask")
    enter_subnet()

def calculate_range(network_ip):
    counter = 0
    # loop through odd numbers
    for last_octet in range(255, 1, -2): # starts at 255, goes down till 1, goes down by 2
                                         # (255 not counted due to being broadcast addr)
        counter += 1
        if counter <= 10: # first 10 ips reserved for printers and servers
            pass
        else:
            full_ip = f"{network_ip}.{last_octet}"
            if host_up(full_ip): # if the host is up
                pass
                #scan_ports(network_ip, last_octet) # scan ports

def host_up(full_addr: str): # function to determine if a host is up
    # returns true or false if the host is up or not
    # checks if host can be pinged
    if system("ping -c 1 " + full_addr) == 0: # if host responds when pinged
        print("Host is up")
        return True
    else: # ping failed, either host is down or has blocked pings
        # try on http port
        print("Ping failed, port connection attempt in progress")
        port = 80
    
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)   
        # returns an error indicator
        print(f"Connecting to {full_addr}:{port}")
        result = s.connect((full_addr,port))
        if result == None:
            print("Host is down")
            return False
        elif result == 0:
            print(f"Port {port} is open")
            s.close()
            return True
    return False

def scan_ports(network_ip, host_ip):
    target = f"{network_ip}.{host_ip}" # defines target ip address to scan
    print(target)
    for port in range(60000):
        print(port)
        try:
            target = gethostbyname(target)
        except Exception as error:
            print(f"Error occurred\n{error}")
        else:
            print("Host name retrieved succesfully")
        
        print(f"Connecting to {target}:{port}")
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)   
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    

banner = ascii_text.figlet_format("ROI PORT SCANNER")
print(banner)

enter_ip()
# enter_subnet()


global logs 
logs = []

