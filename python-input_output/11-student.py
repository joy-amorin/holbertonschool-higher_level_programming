#!/usr/bin/python3
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

    def to_json(self, attrs=None):
        """
        Public method def  that retrieves a dictionary
        representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        if len(json) > 0:
            self.first_name = json.get('first_name')
            self.last_name = json.get('last_name')
            self.age = json.get('age')