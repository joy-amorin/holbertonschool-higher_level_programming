#!/usr/bin/python3
"""
define class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)
