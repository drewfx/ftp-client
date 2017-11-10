#!/usr/bin/env python
# Server
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print "The server is read to receive"

# The buffer to store the received data
data = ""

# Forever accept incoming connections
while 1:
    # Accept a connection
    connectionSocket, addr = serverSocket.accept()
    tempBuffer = ""
    data = ""

    while len(data) != 40:
        # Receive data
        tempBuffer = connectionSocket.recv(40)
        data += tempBuffer

    print data
    connectionSocket.close()
