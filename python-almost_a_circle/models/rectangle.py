#!/usr/bin/python3
"""
define class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """public method that returns the area"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="")
            print()
