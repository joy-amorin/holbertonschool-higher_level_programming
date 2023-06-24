#!/usr/bin/python3
""" define a function to read a file
"""


def read_file(filename=""):
    """function to read a file"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
