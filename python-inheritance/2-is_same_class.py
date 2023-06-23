#!/usr/bin/python3
"""
check if a onbject is as instance of the class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class
    """

    return type(obj) is a_class
