#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """method to print list sorted"""
        print(sorted(self))
