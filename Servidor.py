import socket

localIP = "127.0.0.1"
locport = 20001
tamBuff = 1024

serverUDP = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
serverUDP.bind((localIP,locport))

print("WORKING...\n")

while True:
    dataReceive = serverUDP.recvfrom(tamBuff)
    msgRecibido = dataReceive[0]
    origenAdres = dataReceive[1]

    print("MESSAGE: ",msgRecibido.decode(),sep = '')
    print("ADDRESS: {}".format(origenAdres),end = "\n\n")