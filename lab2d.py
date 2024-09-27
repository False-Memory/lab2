# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: September 27th, 2024
# Learn how to use command line arguments.
# Purpose: .
# Usage: ./lab2d.py
import sys

# TO DO 1: copy the required lines from README.md to print version, platform, argv and the length of argv.
# run the script in the terminal using command: python ./lab2d.py

print(sys.version)      # prints the current version of python being used
print(sys.platform)     # prints the name of the operating system.
print(sys.argv)         # prints the list of all arguments given at the command line when running the python script
print(len(sys.argv))    # tells us the number of command line arguments the user has provided

# TO DO 2: copy the required lines from README.md to print argv[0], argv[1] and argv[2]
# run the script using the following command: python lab2d.py maija Maija

print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument.
print(sys.argv[2]) # prints the third argument.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.