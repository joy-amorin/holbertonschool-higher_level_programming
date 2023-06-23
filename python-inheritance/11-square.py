#!/usr/bin/python3
"""define a Square class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """return area"""

        return self.__size ** 2

    def __str__(self):
        """return str"""

        return f"[Square] {self.__size}/{self.__size}"
