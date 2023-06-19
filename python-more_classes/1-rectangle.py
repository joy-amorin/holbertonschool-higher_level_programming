#!/usr/bin/python3
"""Define a
Square class
"""


class Rectangle:
    """
    class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        init
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
