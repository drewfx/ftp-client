#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :clientftpinterface.py
# description     :FTP Interface class to handle requests and descriptions of commands
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :
# notes           :commands must be declared using the do_* method format to be accepted
# python_version  :2.7.12
##################################################

# Import modules
from cmd import Cmd
from sys import exit
from os import system
import constants as const
import re
import os.path


class ClientFtpInterface(Cmd):
    """Simple FTP prompt for client"""

    socket = ''
    prompt = "ftp> "
    intro = "Type: 'help' for a list of commands"

    ################################
    #    Prompt Command Methods    #
    ################################
    def do_get(self, args):
        """Get command structure for downloading a file form the host"""
        filename = self.get_file_name(args)

        # loop to get file from server
        if filename:
            self.socket.send("%s %s" % (const.COMMAND_GET, filename))
            self.receive_file()
        else:
            print "Incorrect usage, type 'help' for formatting."

    def do_put(self, args):
        """Put command structure for uploading a file to the host"""
        response = self.make_request(const.COMMAND_PUT)
        print response

    def do_ls(self, args):
        """Query command for host file listing in ftp directory"""
        response = self.make_request(const.COMMAND_LS)
        print response

    def do_clear(self, args):
        """Clears the prompt"""
        system('clear')
        return

    def do_quit(self, args):
        """Quits the program"""
        response = self.make_request(const.COMMAND_QUIT)
        exit(response)

    ################################
    #    Command Helper Methods    #
    ################################
    def help_get(self):
        """Describes the get command"""
        self.print_help_method("get", "Download file from host", "get <file>")
        return

    def help_put(self):
        """Describes the put command"""
        self.print_help_method("put", "Upload file from host", "put <file>")
        return

    def help_ls(self):
        """Describes the ls command"""
        self.print_help_method("ls", "List files on the host", "ls")

    def help_clear(self):
        """Describes the clear command"""
        self.print_help_method("clear", "Clear the terminal", "clear")

    def help_quit(self):
        """Describes the quit command"""
        self.print_help_method("quit", "Quits the interface", "quit")

    ################################
    #        Utility Methods       #
    ################################
    def emptyline(self):
        """This overrides the default action for when an emptyline is
        submitted via the prompt window.
        """
        pass

    def print_help_method(self, command, description, example):
        """This prints the formatted help description for a command"""
        msg = "\nHelp for command: %s" \
              "\n========================================" \
              "\n  -Description: %s" \
              "\n  -Example: %s" % (command, description, example)
        print msg

    def store_cmd_socket(self, socket):
        self.socket = socket

    def make_request(self, cmd):
        """Send request to server"""
        self.socket.send(cmd)
        response = self.socket.recv(const.BUFFER_SIZE)
        return response

    def get_file_name(self, args):
        """Gets filename from input string
        :type args string
        :rtype regex match substring
        """
        reg = re.compile("(\w*\.\w*)")
        match = reg.match(args)
        if match:
            return match.group()
        else:
            return None

    def receive_file(self):
        """Receive file from the server"""
        header = self.receive_bytes(10)
        file_size = int(header)
        print "Receiving... %d of data." % file_size
        file_data = self.receive_bytes(file_size)
        # TODO: handle file f = open(filename, 'wb')


    def send_file(self):
        """Send file to the server"""

    def receive_bytes(self, size=None):
        """Receives size number of bytes from server
        :type size integer
        :rtype received string
        """
        # if a size is passed
        if size:
            # initialize local vars
            temp_buffer = ""
            received = ""

            # read input
            while len(temp_buffer) < size:
                temp_buffer = self.socket.recv(size)

                # if nothing returns
                if not temp_buffer:
                    print "Error: no bytes received from server."
                    break

                # add to received
                received += temp_buffer

            return received
        else:
            print "Error: receive size error."
