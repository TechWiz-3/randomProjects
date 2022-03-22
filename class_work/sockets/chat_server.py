import socket
import sys

host = 'www.tafensw.edu.au'
port = 80 # web# create socket
print('# Creating socket')
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()# Connect to remote server

print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))# Send data to remote server
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print ('Send failed')
    sys.exit()# Receive data

print('# Receive data from server')
reply = s.recv(4096)
print(reply)




# import socket



# # Set up a TCP/IP socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



# # Connect as client to a selected server
# # on a specified port
# s.connect(("www.tafensw.edu.au",80))



# # Protocol exchange - sends and receives
# s.send("GET /robots.txt HTTP/1.0\n\n")
# while True:
# resp = s.recv(1024)
# if resp == "": break
# print resp,



# # Close the connection when completed
# s.close()
# print "\ndone"

# [12:58 pm] Kiran Fatima
# # get the hostname
# host = socket.gethostname() # initiate port no above 1024
# port = 5000 # get instance
# server_socket = socket.socket()
# # look closely - the bind() function takes tuple as argument
# # bind host address and port together
# server_socket.bind((host, port)) # configure how many clients the server can listen to simultaneously
# server_socket.listen(2) # accept new connection
# conn, address = server_socket.accept()
# print("Connection from: " + str(address))
# while True:
# # receive data stream - it won't accept a data packet greater than 1024 bytes
# data = conn.recv(1024).decode()
# if not data:
# # if data is not received, break out of loop
# break
# print("from connected user: " + str(data))
# data = input(' -> ') # send data to the client
# conn.send(data.encode()) # close the connection
# conn.close()

