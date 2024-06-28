#!/usr/bin/python3

"""defining a class `Square`"""


class Square:
    """
    `Square` represents a typical geometrical square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """retrieves the attribute"""
        return self.__size

    @size.setter
    def size(size, value):
        """modify the attribute value"""

        if type(value) is not int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculates area of the square"""
        return self.__size ** 2
