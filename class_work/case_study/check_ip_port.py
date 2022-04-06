# Author’s name
# Email address 
# Copyright (as 'Copyright Red Opal Innovations')
# License (as 'Proprietary') 
# Last updated date
# Version (numbered starting 1.0.1)
# Status (set initially to 'development') 
# An overview of the script's logic

"""
Global variables: logs[], overwrite_ip_target (for testing)
"""

# Imports

from socket import (
    inet_aton as valid_ipv4,
    AF_INET as ipv4,
    SOCK_STREAM as tcp,
    setdefaulttimeout,
    socket
)
import pyfiglet as ascii_text
from datetime import datetime
import syslog
from os import system
import threading

logs = []  # list used for storing logs


# Function for writing to log file
def log(payload):
    """Function for logging events as required"""
    logs.append(payload)  # adds the payload to the logs list
    print(payload)  # print to console
    
    try:
        file = open("ip_port_log.txt", "a")  # open log in append mode
        file.write(f"{payload}\n")  # write the payload
        file.close()  # close the file
    except Exception as error:  # if an error occurs
        print(f"Error occured\n{error}")  # print error


# Function for accepting a valid network IP address
def enter_ip():
    netw_addr = input(
        "Enter a valid class C network IP address with the first 3 octets "
            )
    # initial IP address validity check
    try:
        if valid_ipv4(f"{netw_addr}.1"):  # if ip address is valid
            print("IP address passed first check")  # ip address valid (broad)
    except OSError:  # if ip address not valid
        print("IP address invalid, please re-enter")  # ip address not valid
        # call the function to start again, this will repeat until a valid ip address is entered
        enter_ip()

    # secondary, more specific ip address check
    list_netw_addr = netw_addr.split(".")  # splits each octet into a list variable
    list_netw_addr = [int(x) for x in list_netw_addr]  # converts octets in list to strings
    octet_count = len(list_netw_addr)  # gets the number of octets in the provided address
    print("Second IP address check in progress")
    if octet_count == 3:  # check to make sure 3 octets have been provided
        # set each octet a more accessible variable name
        first_octet = list_netw_addr[0]; second_octet = list_netw_addr[1]; third_octet = list_netw_addr[2]
        # ensure the 3 octets have the correct ipv4 class C values
        if (
            223 >= first_octet >= 192 and
            255 >= second_octet >= 0 and
            255 >= third_octet >= 0
        ):
            print("Provided IP address has the correct number of octets and the correct octet values") # ip address valid
            # calculate (and scan) the ip range and exit function
            return calculate_range(f"{first_octet}.{second_octet}.{third_octet}")

        print("IP address range not valid, try again") # notifies user
        enter_ip()  # calls the function again
    # runs if wrong number of octets entered
    print("You haven't entered the correct number of octets, try again") # notifies user
    enter_ip()  # calls the function again


def enter_subnet():
    subnet = input("Enter the subnet mask in extended form: ")
    subnet_list = subnet.split(".")  # split each octet into a list element
    subnet_list = [int(x) for x in subnet_list]  # convert octet elements to integers
    # define more accessible list variables
    first_octet = subnet_list[0]; second_octet = subnet_list[1]; third_octet = subnet_list[2]; fourth_octet = subnet_list[3]
    if (
        first_octet == 255 and
        second_octet == 255 and 
        third_octet == 255 and
        fourth_octet == 0
    ):
        return print("Valid subnet mask entered")
    print(
        "Invalid subnet mask entered, please ensure you enter the class C subnet mask"
        )
    enter_subnet()


def calculate_range(network_ip):
    counter = 0
    # loop through odd numbers
    for last_octet in range(255, 0, -2): # starts at 255, goes down till 1, goes down by 2
                                         # (255 not counted due to being broadcast addr)
        counter += 1
        if counter <= 5: # first 10 (5*2) ips reserved for printers and servers
            pass
        else:
            full_ip = f"{network_ip}.{last_octet}"
            if host_up(full_ip):  # if the host is up
                print(f"Host {full_ip} is up\nPort scanning commencing")
                print("-"*20)
                scan_ports(network_ip, last_octet) # scan ports
            else:
                print(f"{full_ip} is currently down or doesn't exist")


def host_up(full_addr: str):  # function to determine if a host is up
    # returns true or false if the host is up or not
    # checks if host can be pinged
    if (
        system(f"ping -c 1 {full_addr} >/dev/null 2>&1") == 0
            ):  # if host responds when pinged
        # host is up
        return True
    # host not responding to pings
    return False  # assume host is down and return false


def scan_ports(network_ip, host_ip):
    target = f"{network_ip}.{host_ip}"  # defines target ip address to scan
    print(target)
    #for port in range(65535): # <-- if all ports must be scanned
    with open("ports.txt", "r") as ports:
        for port in ports:
            port = int(port)
            print(f"Connecting to {target}:{port}")
            s = socket(ipv4, tcp)
            setdefaulttimeout(1)
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result == 0:
                time = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
                log_payload = f"IP: {target}:{port} OPEN {time}"
                log(log_payload)
            else:
                time = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
                log_payload = f"IP: {target}:{port} CLOSED {time}"
                log(log_payload)
            s.close()

if __name__ == "__main__":
    banner = ascii_text.figlet_format("PORT SCANNER")
    print(banner)

    enter_ip()
    # enter_subnet()
