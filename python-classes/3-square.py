#!/usr/bin/python3
"""Defian Suare Class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """init method, size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Square area"""
        return self.__size * self.__size
