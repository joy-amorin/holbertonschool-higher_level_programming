#!/usr/bin/python3
"""
check is a bnject is an instance of
or is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    t returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from,
    the specified class
    """
    return isinstance(obj, a_class)
