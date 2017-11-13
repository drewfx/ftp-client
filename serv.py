#!/usr/bin/env python
import socket
import sys
import commands


def run(serve_port):
    """Start our FTP server and
    Listen for client connections.
    """
    print_help()
    server_connection = initialize(serve_port)
    listen(server_connection)


def initialize(serve_port):
    """Server initialization
    :type serve_port
    """
    try:
        server_port = int(serve_port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', server_port))
        server_socket.listen(1)
        print "Server has been initialized, listening on port " + str(server_port)
    except socket.error as serr:
        raise serr
    return socket


def listen():
    """Listen for clients"""
    while 1:

        print("Accepted connection from client")



def print_help():
    """Print instructions"""
    help = "#####################" \
           "#    FTP COMMANDS   #\n" \
           "#####################\n" \
           "help: print help\n" \
           "get: download file <file_name>\n" \
           "put: upload file<file_name>\n" \
           "ls: lists directory\n" \
           "quit: disconnects from the server\n" \
    print(help)


def initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    print("Example usage: python serv.py <port number>")


# Run
if __name__ == '__main__':
    args = sys.argv
    arg_length = len(args)
    if arg_length == 2:
        run(args[1])
    else:
        if arg_length == 1:
            raise ValueError("Argument Exception: You are missing the socket parameter.\n")
        if arg_length > 2:
            raise ValueError("Argument Exception: Your arguments exceed the the required parameters.\n")
        initialization_prompt()
