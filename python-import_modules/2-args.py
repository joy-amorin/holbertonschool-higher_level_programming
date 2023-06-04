#!/usr/bin/python3

from sys import argv

args = argv[1:]

if len(args) == 0:

    print("{} arguments.".format(len(args)))
elif len(args) == 1:
    print("{} argument:".format(len(args)))
else:
    print("{} arguments:".format(len(args)))
for arg in range(len(args)):
    print("{}: {}".format(arg + 1, args[arg]))
