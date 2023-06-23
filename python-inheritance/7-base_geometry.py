#!/usr/bin/python3
"""
define a BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method integer validator"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
