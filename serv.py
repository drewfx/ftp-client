#!/usr/bin/env python
import socket
import sys

def run():
    """Start our FTP server and
    Listen for client connections.
    """
    initialize()


def initialize():
    """Server initialization"""
    try:
        server_port = 12000
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind(('', serverPort))
        server_socket.listen(1)
        print "Server has been initialized, listening on port" + server_port
    except error as serr:
        raise serr




# Run
if __name__ == '__main__':
    run()
