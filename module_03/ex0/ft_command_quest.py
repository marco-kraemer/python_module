#!/usr/bin/env python3

import sys

arguments = sys.argv
if len(arguments) == 1:
    print("No arguments provided!")
print(f"Program name: {arguments[0]}")
i = 0
if not len(arguments) == 1: 
    print(f"Arguments received: {len(arguments) - 1}")
for argument in arguments:
    if not i == 0:
        print(f"Argument {i}: {argument}")
    i += 1
print(f"Total arguments: {len(arguments)}")
