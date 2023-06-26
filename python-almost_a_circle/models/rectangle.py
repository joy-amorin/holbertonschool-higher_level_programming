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

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        self.__width = width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        self.__x = y
