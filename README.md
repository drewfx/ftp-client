# ftp server and client
Simple ftp server and client used locally to communicate and transfer
files between cli.  Written for CPSC 471 at CSUF using Python

__Author:__ Andrew Ruppel</br>
__Class:__ CPSC 471</br>
__Professor:__ Yun Tian</br>
__Date:__ 11/26/2017</br>
__Language:__ Python</br>


### Prerequisites
No special requirements.

Python 2.7.x</br>
Built and tested on Ubuntu 16.04 LTS

### Installing
No installation necessary.</br>
All files are referenced and part of the core Python libraries.

### Usage
Successfully tested using 'localhost' and 127.0.0.1

Invoke the server:
```bash
python serv.py <port number>
```
Invoke the client:
```bash
python cli.py <server address> <port number>
```
Tested Methods:
* get - get (filename)
* put - put (filename)
* ls - list directory of ftp server
* clear - clear cli
* help - lists help guide for commands 'help' or 'help <command>'
* quit - exits (client only)

Has handled most errors that have occurred, although streamlining the error handling for the sockets could definitely be improved and overall, the structure could be more modular.

### Notes
It is a tad messy at the current state, with more time and refactoring it could be made to be a more stable, and complete, ftp system.

The current version, 0.1, is a very rough first attempt at socket programming and handling socket interactions between a server and client.
