import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET : Internet address family for IPv4
# AF_INET6: Internet address family for IPv6
# SOCK_STREAM : socket type for TCP
# SOCK_DGRAM : socket type for UDP
server_addr='192.168.1.100'#socket.gethostbyname(socket.gethostname())

port=1234
s.bind((server_addr, port)) #  s.bind(('127.0.0.1', 1234))
# socket.gethostname() translates a host name to IPv4 address (type string)

s.listen(5)

while True:
    clientSocket, clientAddress=s.accept()
    print(f"connection form {clientAddress} has been established")
    clientSocket.send("welcome to server".encode("utf-8"))

# import socket
# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # AF_INET : Internet address family for IPv4
# #  AF_INET6: Internet address family for IPv6
# # SOCK_STREAM : socket type for TCP
# # SOCK_DGRAM : socket type for UDP
# # socket.gethostname() translates a host name to IPv4 address (type string)
# server_addr=socket.gethostbyname(socket.gethostname())
# port=1234
# s.bind((server_addr, port))            #  s.bind(('127.0.0.1', 1234))

# s.listen(5)
# while True:
#     clientSocket, clientAddress = s.accept()
#     print("connection form {} has been established".format(clientAddress))
#     clientSocket.send("welcome to server".encode("utf-8"))


# host = '192.168.1.100' # as both code is running on same pc
# port = 5000 # socket server port number

# client_socket = socket.socket() # instantiate
# client_socket.connect((host, port)) # connect to the server

# message = input(" -> ") # take input

# while message.lower().strip() != 'bye':
#     client_socket.send(message.encode()) # send message
#     data = client_socket.recv(1024).decode() # receive response

#     print('Received from server: ' + data) # show in terminal



#     message = input(" -> ") # again take input



# client_socket.close() # close the connection