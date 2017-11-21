#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :hostftpinterface.py
# description     :Server side operations of local FTP server
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :
# notes           :
# python_version  :2.7.12
##############################

import socket
import sys
from commands import getstatusoutput


class HostOperations:
    """Perform server side actions such as list dir, put/get file"""

    def __init__(self, client_socket):
        """Initialize with client socket"""
        self.client_socket = client_socket

    ################################
    #        Command Methods       #
    ################################
    def do_get(self, args):
        """Op method for sending a file to the client"""
        self.client_socket.send("GET")

    def do_put(self, args):
        """Op method for receiving a file from the client"""
        self.client_socket.send("PUT")

    def do_ls(self):
        """Perform directory listing and return results"""
        results = ""

        # run directory list and return results, or return failure
        try:
            results = getstatusoutput('ls -l')[1]
        except:
            results = "Unable to process command: ls"

        self.client_socket.send(results)

    def do_quit(self):
        """Closes the connection with the client"""
        print "Client 'quit' is successful, closing connection."
        self.client_socket.send("Thanks for connection. Bye.")
        self.client_socket.close()

    ################################
    #     Command Help Methods     #
    ################################
    def receive_file(self):
        """Receive the file from the client and upload to folder"""
        # TODO:
        return

    def send_file(self):
        """Get file from host and send to client"""
        # TODO:
        return

    def op_succcess_message(self):
        """"""
        # TODO:

    def op_failure_message(self):
        """"""
        # TODO:
