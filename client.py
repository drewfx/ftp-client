# Client
from socket import *

serverName = "ecs.fullerton.edu"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

data = "Hello world! This is some stuff"

clientSocket.send(data)

clientSocket.close();
