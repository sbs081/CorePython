from socket import *
#不需要和服务器建立链接直接把消息发出去然后等待服务器的回复。
HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    data = data.encode()
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)

udpCliSock.close()