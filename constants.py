#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :constants.py
# description     :declared constants
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :
# notes           :
# python_version  :2.7.12
##############################

FILE_SEPARATOR = '/'

# Commands
COMMAND_LS = 'ls'
COMMAND_GET = 'get'
COMMAND_PUT = 'put'
COMMAND_QUIT = 'quit'

# Accepted client commands
ACCEPTED_COMMANDS = (COMMAND_LS, COMMAND_GET, COMMAND_PUT, COMMAND_QUIT)

# FTP folder attributes
CLIENT_DOWNLOAD_FOLDER = './_client_downloads'
CLIENT_UPLOAD_FOLDER = './_client_uploads'

# Buffer Constant for sockets
HEADER_SIZE = 10
BUFFER_SIZE = 4096
