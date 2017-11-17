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
##############################

# Import modules
import cmd
import sys


class FtpInterface(cmd.Cmd):
    """Simple FTP prompt for client"""

    prompt = "ftp> "
    intro = "Type: 'help' for a list of commands"

    def start(self):
        self.cmdloop("1")

    def do_get(self, args):
        """"""
        return

    def do_put(self, args):
        """"""
        return

    def do_ls(self, args):
        """"""
        return

    def do_quit(self, args):
        """Quits the program"""
        sys.exit("Quitting...Goodbye.")

    def do_EOF(self):
        return True

    def help_get(self):
        print "Download a file"
        return

    def help_put(self):
        print "Upload a file"
        return

    def help_ls(self):
        print "List FTP directory files"

    def emptyline(self):
        pass
