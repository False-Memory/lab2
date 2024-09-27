# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: September 27th, 2024
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py
import sys
# TO DO 1: Follow the instructions given in README.md file
if len(sys.argv) < 3:
    print("The script requires at least 2 arguments")
else:
    name = sys.argv[1]
    age = sys.argv[2]
    print("Hi",name,",you are",age,"years old and the script recieved",len(sys.argv)-1,"arguments")