#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :cli.py
# description     :FTP Interface class to handle requests and descriptions of commands
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :
# notes           :external class utilized by cli.py
# python_version  :2.7.12
##################################################

# Import modules
from cmd import Cmd
from sys import exit
from os import system


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
        return

    def do_put(self, args):
        """Put command structure for uploading a file to the host"""
        return

    def do_ls(self, args):
        """Query command for host file listing in ftp directory"""
        return

    def do_clear(self, args):
        """Clears the prompt"""
        system('clear')
        return

    def do_quit(self, args):
        """Quits the program"""
        exit("Quitting...Goodbye.")

    ################################
    #     Command Help Methods     #
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

    def store(self, socket):
        self.socket = socket
