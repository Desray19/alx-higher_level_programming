#!/usr/bin/python3
"""
this module is a representation of rectangle Class
"""


class Rectangle():
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        arguments:
            width: rectangle wodth.
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or Sets rectangle wodth."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Gets or Sets rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
