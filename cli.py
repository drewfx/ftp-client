#!/usr/bin/env python
import socket
import sys


def run(cli_args):
    """Start our FTP server and
    Listen for client connections.
    :type cli_args user input arguments
    """
    port = check_input(cli_args)
    ftp_socket = initialize_connection(port)


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


def initialize_connection(port):
    """Connect to server
    :type port string
    :rtype ftp_socket socket._socketobject
    """
    try:
        server_port = int(port)
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.bind(('', server_port))
        ftp_socket.listen(1)
        print "Connection to server has been established on port " + str(server_port) + ".\n"
    except socket.error as serr:
        raise serr
    return ftp_socket


def initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    print "Example usage: python cli.py <port number>"


# Run
if __name__ == '__main__':
    run(sys.argv)
