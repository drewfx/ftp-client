#!/usr/bin/env python
import socket
import sys
import commands


def run(cli_args):
    """Start our FTP server and
    Listen for client connections.
    :type cli_args user input arguments
    """
    port = check_input(cli_args)
    ftp_socket = initialize(port)
    listen(ftp_socket)


def check_input(cli_args):
    """Check user input to start the server for correct
    number of parameters.
    :type cli_args user input
    :rtype cli_args[port]
    """
    arg_length = len(cli_args)
    if arg_length == 2:
        return cli_args[1]
    else:
        if arg_length == 1:
            sys.exit("Argument Exception: You are missing the socket parameter.\n")
        if arg_length > 2:
            sys.exit("Argument Exception: Your arguments exceed the the required parameters.\n")
        initialization_prompt()


def initialize(port):
    """Server initialization
    :type port string
    :rtype ftp_socket socket._socketobject
    """
    try:
        server_port = int(port)
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.bind(('', server_port))
        ftp_socket.listen(1)
        print "Server has been initialized, listening on port " + str(server_port)
    except socket.error as serr:
        raise serr
    return ftp_socket


def listen(ftp_socket):
    """Listen for clients
    :type ftp_socket int
    """
    while 1:
        print("Accepted connection from client")
        break;
    ftp_socket.close();



def print_help():
    """Print instructions"""
    help = "###############################\n" \
           "#         FTP COMMANDS        #\n" \
           "###############################\n" \
           "help: print help\n" \
           "get <filename>: downloads a file <file_name>\n" \
           "put <filename>: uploads a file <file_name>\n" \
           "ls: lists directory\n" \
           "quit: disconnects from the server\n"
    print help


def initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    print("Example usage: python serv.py <port number>")


# Run
if __name__ == '__main__':
    run(sys.argv)
