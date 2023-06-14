#!/usr/bin/python3
"""
add two numbers and return the result


"""


def add_integer(a, b=98):
    """
    check if the numers ar integers, cast to int if they are float
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    sum = a + b
    return sum
