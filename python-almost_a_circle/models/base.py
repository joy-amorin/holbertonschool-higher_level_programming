#!/usr/bin/python3
"""
define a class Base
"""
import json
import os


class Base:
    """clase Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file:
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dict = []

        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        json_str = cls.to_json_string(list_dict)

        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all
        attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"

        if os.path.exists(filename):
            with open(filename, "r") as f:
                list_obj = cls.from_json_string(f.read())
                list_instance = [cls.create(**obj) for obj in list_obj]
            return list_instance
        return []
