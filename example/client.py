#!/usr/bin/env python
# Client
from socket import *

serverName = "ecs.fullerton.edu"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

data = "Hello world! This is some stuff"

while bytesSent != len(data):
    bytesSent += clientSocket.send(data[bytesSent :])

clientSocket.close();
