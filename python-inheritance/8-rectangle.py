#!/usr/bin/python3
"""
define class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ Instantiation with width and height"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
