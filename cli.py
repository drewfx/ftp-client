#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :cli.py
# description     :Client side operations of local FTP server
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :python cli.py <address/ip> <port>
# notes           :
# python_version  :2.7.12
##############################

# Import modules
import socket
import sys
from clientftpinterface import ClientFtpInterface


def run(cli_args):
    """Start our FTP server and
    Listen for client connections.
    :type cli_args user input arguments
    """
    # get our address and port from input, or throw error
    address, port = get_server_parameters(cli_args)
    # initialize the ftp command connection
    command_socket = initialize_command_connection(address, port)
    # command structure for client
    handle_client_requests(command_socket)


def get_server_parameters(cli_args):
    """Check user input to start the server for correct
    number of parameters.
    :type cli_args user input
    :rtype cli_args[port]
    """
    arg_length = len(cli_args)
    if arg_length == 3:
        return cli_args[1], cli_args[2]
    else:
        if arg_length == 1:
            print "\nArgument Exception: You are missing the address and port parameters."
        if arg_length == 2:
            print "\nArgument Exception: You are missing the socket parameter."
        if arg_length >= 4:
            print "\nArgument Exception: Your arguments exceed the the required parameters."
        initialization_prompt()


def initialize_command_connection(server_address, server_port):
    """Connect to server
    :type server_address string
    :type server_port string
    :rtype ftp_socket socket._socketobject
    """
    server_port = int(server_port)

    # try-except to create socket
    try:
        ftp_cmd_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as socket_error:
        print "Socket Error: %s" % socket_error
        sys.exit()

    # try-except to establish connection to the host machine
    try:
        ftp_cmd_socket.connect((server_address, server_port))
        print "\nConnection to server has been established on port %s ." % server_port
    except socket.error as socket_error:
        print "Socket Error: %s" % socket_error
        sys.exit()

    # return our Command socket if successful
    return ftp_cmd_socket


def handle_client_requests(command_socket=None):
    """Handle all client related queries to the host"""
    if command_socket is not None:
        # Create our client interface and store cmd socket
        ftp_interface = ClientFtpInterface()
        ftp_interface.store_cmd_socket(command_socket)
        ftp_interface.cmdloop()


def initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    message = "\nUsage: python cli.py <server address> <server port>" \
              "\n\t- server address: address or ip" \
              "\n\t- server port:    port number" \
              "\nExample: python cli.py ecs.fullerton.edu 1200"
    sys.exit(message)


# Run
if __name__ == '__main__':
    run(sys.argv)
