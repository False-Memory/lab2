# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: September 27th, 2024
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

import sys

# TO DO 1: Follow the instructions given in README.md file
print(len(sys.argv))    # tells us the number of command line arguments the user has provided

if len(sys.argv) == 3:
    print("Hello User, Good Job, you provided two arguments!")
elif len(sys.argv) == 1:
    print("This cript requires exactly two arguments. No arguments were provided!")
else:
    print("This script requires exactly two arguments. You provided",len(sys.argv)-1,"arguments.")
