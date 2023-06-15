#!/usr/bin/python3
"""
function that prints a square with the character #

"""


def print_square(size):
    """
    function to print
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if float(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * (size))
