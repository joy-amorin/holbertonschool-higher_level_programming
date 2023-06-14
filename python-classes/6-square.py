#!/usr/bin/python3
"""Defian Square Class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init method, size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """Square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @property
    def position(self):
        """return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
