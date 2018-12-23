from socket import *
import os

HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # connect to server
    tcpCliSock.connect(ADDR)
    
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s%s' % (data, os.linesep))
    # receive data
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()