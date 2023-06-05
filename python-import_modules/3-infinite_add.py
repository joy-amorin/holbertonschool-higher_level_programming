#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    args = argv[1:]
    _sum = 0

    for i in range(len(args)):
        _sum = _sum + int(args[i])

    print("{}".format(_sum))
