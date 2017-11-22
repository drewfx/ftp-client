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

import os.path
import socket
import re
import constants as const
from commands import getstatusoutput


class HostOperations:
    """Perform server side actions such as list dir, put/get file"""

    def __init__(self, client_socket):
        """Initialize with client socket
        :type client_socket socket._socketobject
        """
        self.client_socket = client_socket

    ################################
    #        Command Methods       #
    ################################
    def do_get(self, request):
        """Op method for sending a file to the client
        :type request string
        """
        filename = self.get_file_name(request)
        exists = os.path.isfile("%s%s%s" % (const.CLIENT_UPLOAD_FOLDER, const.FILE_SEPARATOR, filename))

        if filename and exists:
            # Send file and flag success
            self.send_file(filename)
            self.op_success_message(const.COMMAND_GET)
        else:
            # Send error message back to client if no file exists
            self.op_failure_message(const.COMMAND_GET)
            self.client_socket.send(self.buffer_header("0"))

    def do_put(self, request):
        """Op method for receiving a file from the client
        :type request string
        """
        self.client_socket.send("PUT")

    def do_ls(self):
        """Perform directory listing and return results"""
        results = ""

        # run directory list and return results, or return failure
        try:
            results = getstatusoutput('ls -l ./_client_uploads')[1]
            self.op_success_message(const.COMMAND_LS)
        except:
            results = "Unable to process command: ls"
            self.op_failure_message(const.COMMAND_LS)
        # return message to client
        self.client_socket.send(results)

    def do_quit(self):
        """Closes the connection with the client"""
        self.op_success_message(const.COMMAND_QUIT)
        self.client_socket.send("Thanks for connection. Bye.")
        self.client_socket.close()

    ################################
    #    Command Helper Methods    #
    ################################
    def receive_file(self):
        """Receive the file from the client and upload to folder"""
        # TODO:
        return

    def send_file(self, filename):
        """Get file from host and send to client
        :type filename string
        """
        # use with to ensure file is closed after ops
        with open(filename, 'rb') as file_object:
            # byte counter
            bytes_sent = 0
            # file data
            data = file_object.read()
            # header with count of bytes in file
            header = self.buffer_header(data)
            # prepend the header
            file_data = header + data

            while len(file_data) > bytes_sent:
                try:
                    bytes_sent += self.client_socket.send(file_data[bytes_sent:])
                    self.op_success_message(const.COMMAND_GET)
                except socket.error as e:
                    self.op_failure_message(const.COMMAND_GET)

    def op_success_message(self, command):
        """Print success message"""
        print "SUCCESS: executing %s" % command

    def op_failure_message(self, command):
        """Print failure message"""
        print "FAILURE: executing %s" % command

    def get_file_name(self, client_request):
        """Gets filename from input string
        :type client_request string
        :rtype regex match substring
        """
        reg = re.compile("(\w*\.\w*)")
        match = reg.match(client_request)
        if match:
            return match.group()
        else:
            return None

    def buffer_header(self, header):
        """Buffer the header of a file transfer or response
        :type header string
        :rtype data_size string (padded)
        """
        data_size = str(len(header))
        while len(data_size) < 10:
            data_size = "0" + data_size
        return data_size
