import socket
ipv4 = socket.AF_INET
tcp = socket.SOCK_STREAM 

# s=socket.socket(ipv4, tcp)
# # ip address of the server

# server_addr='192.168.1.100'#socket.gethostbyname(socket.gethostname())
# #server_addr=socket.gethostbyname(socket.gethostname())
# server_port=1234
# s.connect((server_addr, server_port))


# #client and server are in the same machine
# message= s.recv(1024)
# #pass buffer size torecv
# print(message.decode('utf-8'))

# if message.decode('utf-8') == "welcome to server":
#     message = "thank you server"



# s.close()


host = '192.168.1.100' # as both code is running on same pc
port = 1234 # socket server port number

client_socket = socket.socket() # instantiate
client_socket.connect((host, port)) # connect to the server

message = input(" -> ") # take input

while message.lower().strip() != 'bye':
    client_socket.send(message.encode()) # send message
    data = client_socket.recv(1024).decode() # receive response

    print('Received from server: ' + data) # show in terminal



    message = input(" -> ") # again take input



client_socket.close() # close the connection