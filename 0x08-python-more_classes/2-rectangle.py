#!/usr/bin/python3

"""
This module contains a class `Rectangle` that defines a rectangle
"""


class Rectangle:
    """
    A class used to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """initalizes `Rectangle`"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))
