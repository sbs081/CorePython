from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.send(data.encode(), ADDR).encode()
    data, ADDR = udpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

udpCliSock.close()