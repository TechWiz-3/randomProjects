import socket

client_ip = '192.168.1.103'
client_port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((client_ip, client_port)) # tuple
s.listen(5)
(client_ip, client_port) = s.accept()
# lmao