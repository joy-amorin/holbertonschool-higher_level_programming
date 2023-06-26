#!/usr/bin/python/3
"""
define a Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
         Public method def  that retrieves a dictionary
         representation of a Student instance
        """
        return self.__dict__
