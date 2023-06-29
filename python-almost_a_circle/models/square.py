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
