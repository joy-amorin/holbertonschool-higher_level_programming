#!/usr/bin/python3
""" define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.width}")

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def update(self, *args, **kwargs):
        """Square update"""

        if len(args) > 0:
            attr = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """"return a dictionary representation
        of a Square
        """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
