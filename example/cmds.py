# *********************************************************************
# This file illustrates how to execute a command and get it's output
# *********************************************************************
from commands import getstatusoutput

# Run ls command, get output, and print it
for line in getstatusoutput('ls -l'):
    print line



