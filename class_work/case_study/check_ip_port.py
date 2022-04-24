# Author’s name
# Email address 
# Copyright (as 'Copyright Red Opal Innovations')
# License: Proprietary'
# Last updated date
# v3.20.0
# Status: Development
# Script logic overview:

"""
Global variables: logs[]
"""

# Imports

from genericpath import getsize
from multiprocessing.sharedctypes import Value
from socket import (
    inet_aton as valid_ipv4,
    AF_INET as ipv4,
    SOCK_STREAM as tcp,
    setdefaulttimeout,
    socket
)
import pyfiglet as ascii_text
from datetime import datetime
from syslog import syslog, LOG_NOTICE
from sys import platform as get_os
from os import system
from os.path import getsize
# import win32evtlogutil
# import win32evtlog

logs = []  # list used for storing logs


# Function for writing to log file
def log(payload):
    """
    Function for logging events to log file,
    console and event viewer/system log
        """
    logs.append(payload)  # adds the payload to the logs list
    print(payload)  # print to console
    # log to file
    try:
        file = open("ip_port_log.txt", "a")  # open log in append mode
        file.write(f"{payload}\n")  # write the payload
        file.close()  # close the file
    except Exception as error:  # if an error occurs
        print(f"Error occured\n{error}")  # print error

    if get_os == 'darwin':  # MacOS
        # use syslog for logging
        try:
            syslog(LOG_NOTICE, payload)  # log to /private/var/log/system.log
        except PermissionError:
            err_msg = (
                "Sorry, you do not have the correct"\
                "permissions to write to the system log"
                    )
            print(err_msg)

    elif get_os == 'win32':  # windows OS
        # use win32evtlog for logging
        pass

# Function for accepting a valid network IP address
def enter_ip():
    """Function for entering the network address"""
    netw_addr = input(
        "Enter a valid class C network IP address with the first 3 octets "
            )
    # initial IP address validity check
    try:
        if valid_ipv4(f"{netw_addr}.1"):  # if ip address is valid
            # ip address valid but not confirmed to be a class C IP address
            pass
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


def calculate_range(network_ip):
    """
    Function for calculating the range of
    IP addresses in the network address provided
        """
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
                print("-"*40)
                scan_ports(network_ip, last_octet) # scan ports
            else:
                print(f"{full_ip} is currently down or doesn't exist")


def host_up(full_addr: str):
    """
    Function to determine if a host is up
    Returns true or false if the host is up or not
    Checks if host can be pinged
        """ 
    if (
        system(f"ping -c 1 {full_addr} >/dev/null 2>&1") == 0
            ):  # if host responds when pinged
        # host is up
        return True
    # host not responding to pings
    return False  # assume host is down and return false


def scan_ports(network_ip, host_ip):
    """Scans the specified ports of a provided host"""
    target = f"{network_ip}.{host_ip}"  # defines target ip address to scan
    print(target)
    #for port in range(65535): # <-- if all ports must be scanned
    try:
        with open("ports.txt", "r") as ports:
            if getsize('ports.txt') == 0:
                print("Ports file appears to be empty")
            else:
                for port in ports:
                    try:
                        port = int(port)
                    except ValueError:
                        print(f"The following port entry is not a number: {port}")
                        continue  # skips the line with the port number error and moves on
                    else:  # if no error occurs
                        print(f"Connecting to {target}:{port}")
                        # create a socket connection with a context manager
                        with socket(ipv4, tcp) as s:
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
                            # context manager closes socket connection automatically
    except FileNotFoundError:
        print("Ports file does not exist or it isn't in the current working directory")

if __name__ == "__main__":
    banner = ascii_text.figlet_format("PORT SCANNER")
    print(banner)

    enter_ip()
