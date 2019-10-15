import socket

message = str.encode("All work and no play makes Jack a dull boy.")
dirServ = ("127.0.0.1",20001)

clienteUDP = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
clienteUDP.sendto(message,dirServ)