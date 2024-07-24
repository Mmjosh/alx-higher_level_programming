#!/usr/bin/python3

"""
This module contains a class `Rectangle` that defines
a rectangle
"""


class Rectangle:
    """
    A class used to represent a rectangle

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle

    Methods:
        __init__(self, width, height): initializes the rectangle
        width(self): gets the width of the rectangle
        width(self, value): sets the width
        height(self): gets the height of the rectangle
        height(self, value): sets the height of the rectangle
    """
    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
