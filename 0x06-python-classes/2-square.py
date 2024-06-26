#!/usr/bin/python3

"""define `class Square`"""


class Square:
    """
    `Square` class with a private attribute `size` and raises
    type and value err
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
