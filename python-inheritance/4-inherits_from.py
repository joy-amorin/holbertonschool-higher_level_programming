#!/usr/bin/python3
"""
check subclass of
"""


def inherits_from(obj, a_class):
    """
     function that returns True if the object is an instance of a
     class that inherited
     (directly or indirectly) from the specified class
    """
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
