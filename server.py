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
    #Accept a connection
    connectionSocket , addr = serverSocket.accept();

    # Receive data
    data = connectionSocket.recv(40)

    print data

    connectionSocket.close();
