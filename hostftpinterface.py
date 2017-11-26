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

    def __init__(self, client_socket, host_socket):
        """Initialize with client socket
        :type client_socket socket._socketobject
        :type host_socket socket._socketobject
        """
        self.client_socket = client_socket
        self.host_socket = host_socket

    ################################
    #        Command Methods       #
    ################################
    def do_get(self, request):
        """Op method for sending a file to the client
        :type request string
        """
        # get file name, check if exists at path
        file_name = request.split('|')[1]
        file_path = "%s%s%s" % (const.CLIENT_UPLOAD_FOLDER, const.FILE_SEPARATOR, file_name)
        exists = os.path.isfile(file_path)

        if file_name and exists:
            # Send file and flag success
            self.send_file(file_name, file_path)
            self.op_success_message(const.COMMAND_GET)
        else:
            # Send error message back to client if no file exists
            self.op_failure_message(const.COMMAND_GET)
            self.client_socket.send(self.buffer_header("0"))

    def do_put(self, request):
        """Op method for receiving a file from the client
        :type request string
        """
        self.receive_file()

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
        try:
            transfer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            transfer_socket.bind(('', 0))
            transfer_socket.listen(1)
            transfer_port = transfer_socket.getsockname()[1]
            transfer_port = self.buffer_header(transfer_port)
        except socket.error as e:
            print e
            return

        # send transfer port to client
        try:
            self.client_socket.send(transfer_port)
        except socket.error as e:
            self.op_failure_message(const.COMMAND_GET)
            return

        while True:
            ftp_transfer_socket, address = transfer_socket.accept()
            print "Accepted connection from %s" % str(address)

            if ftp_transfer_socket:
                # file name header handling
                file_name_header = self.receive_bytes(ftp_transfer_socket, const.FILENAME_SIZE)
                file_name = file_name_header.translate(None, '0')
                # file size header handling
                file_size_header = self.receive_bytes(ftp_transfer_socket, const.HEADER_SIZE)
                file_size = int(file_size_header)
                # file data handling
                file_data = self.receive_bytes(ftp_transfer_socket, file_size)

                # calculate potential home of file in _client_uploads
                file_path = "%s%s%s" % (const.CLIENT_UPLOAD_FOLDER, const.FILE_SEPARATOR, file_name)

                # allocate file data
                transfer_file = open(file_path, 'w')
                transfer_file.write(file_data)
                transfer_file.close()
                transfer_socket.close()
                self.op_success_message(const.COMMAND_PUT)
                return

    def send_file(self, file_name, file_path):
        """Get file from host and send to client
        :type file_name string
        :type file_path string
        """
        # use with to ensure file is closed after ops
        with open(file_path, 'r') as file_object:
            # establish ephemeral port
            transfer_port = ''

            # read file, put file size in padded header, prepend header to data
            data = file_object.read()

            try:
                transfer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                transfer_socket.bind(('', 0))
                transfer_socket.listen(1)
                transfer_port = transfer_socket.getsockname()[1]
                transfer_port = self.buffer_header(transfer_port)
            except socket.error as e:
                print e
                self.op_failure_message(const.COMMAND_GET)
                return

            # send transfer port to client
            try:
                self.client_socket.send(transfer_port)
            except socket.error as e:
                self.op_failure_message(const.COMMAND_GET)
                return

            while True:
                print "Listening on %s" % transfer_port
                ftp_transfer, address = transfer_socket.accept()
                print "Accepted connection from %s" % str(address)

                if ftp_transfer:
                    # byte counter
                    bytes_sent = 0

                    file_name_header = self.buffer_header(file_name, const.FILENAME_SIZE)
                    file_size_header = self.buffer_header(str(len(data)), const.HEADER_SIZE)

                    file_data = file_name_header + file_size_header + data

                    while len(file_data) > bytes_sent:
                        try:
                            bytes_sent += ftp_transfer.send(file_data[bytes_sent:])
                        except socket.error as e:
                            print e
                            self.op_failure_message(const.COMMAND_GET)
                            return

                    self.op_success_message(const.COMMAND_GET)
                    ftp_transfer.close()
                    transfer_socket.close()
                    return

    def op_success_message(self, command):
        """Print success message"""
        print "SUCCESS: executing %s" % command

    def op_failure_message(self, command):
        """Print failure message"""
        print "FAILURE: executing %s" % command

    def receive_bytes(self, sock, size=None):
        """Receives size number of bytes from server
        :type sock socket.socketobject
        :type size integer
        :rtype received string
        """
        # if a size is passed
        if sock and size:
            # initialize local vars
            temp_buffer = ""
            received = ""

            # read input
            while len(temp_buffer) < size:
                temp_buffer = sock.recv(size)

                # if nothing returns
                if not temp_buffer:
                    print "Error: no bytes received from server."
                    break

                # add to received
                received += temp_buffer

            return received
        else:
            print "Error: receive size error."

    def buffer_header(self, header, size=10):
        """Buffer the header of a file transfer or response
        :type header string
        :type size int
        :rtype data_size string (padded)
        """
        header = str(header)
        while len(header) < size:
            header = "0" + header
        return header
