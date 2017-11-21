#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :serv.py
# description     :Server side operations of local FTP server
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :python serv.py <port>
# notes           :
# python_version  :2.7.12
##############################

# Import modules
import socket
import sys
from constants import ACCEPTED_COMMANDS
from hostftpinterface import HostOperations


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
        help_initialization_prompt()


def initialize(port):
    """Server initialization
    :type port string
    :rtype ftp_socket socket._socketobject
    """
    try:
        server_port = int(port)
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.bind(('', server_port))
        ftp_socket.listen(2)
        print "Server has been initialized, listening on port %s" % str(server_port)
    except socket.error as socket_error:
        print "Socket Error: %s" % socket_error
        sys.exit()
    return ftp_socket


def listen(ftp_socket):
    """Listen for clients
    :type ftp_socket socket.socket
    """
    while True:
        ftp_client, address = ftp_socket.accept()
        print "Accepted connection from %s" % str(address)

        ops = HostOperations(ftp_client)

        while True:
            client_request = ftp_client.recv(1024)
            print client_request

            # check to see if the client request is a valid command
            if client_request in ACCEPTED_COMMANDS:
                # if we have a valid command run said command
                if client_request == 'ls':
                    ops.do_ls()
                if client_request == 'put':
                    ops.do_put()
                if client_request == 'get':
                    ops.do_get()
                if client_request == 'quit':
                    ops.do_quit()
                    break
            else:
                ftp_client.send("Incorrect commands: %s" % client_request)
    # close our host socket


def help_initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    print "Example usage: python serv.py <port number>"


# Run
if __name__ == '__main__':
    run(sys.argv)
