#!/usr/bin/env python3

import sys
import subprocess

# takes oldFiles.txt as a command line argument
# each line is a file name located in directy ~/data, is the old file name
# replace files with the old file name with the new file name
# new file name is the old file name with "jane" replaced by "jdoe"

# open oldFiles.txt
with open(sys.argv[1], 'r') as oldFiles:
    # use readline() method
    # read one line at a time
    line = oldFiles.readline()
    while line:
        # strip newline character
        line = line.rstrip()
        # create new file name
        newFile = line.replace("jane", "jdoe")
        # replace old files in ~/data with new files
        subprocess.run(["mv", line, newFile])
        # read next line
        line = oldFiles.readline()
# close the file
oldFiles.close()

