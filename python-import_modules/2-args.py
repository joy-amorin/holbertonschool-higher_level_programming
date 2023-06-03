#!/usr/bin/python3

from sys import argv

args = argv[1:]


if len(args) == 1:

    print(len(args), "argument:")
else:
    print(len(args), "arguments:")
for arg in range(len(args)):
    print(arg + 1, ":", args[arg])
