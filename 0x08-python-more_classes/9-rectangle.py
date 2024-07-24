#!/usr/bin/python3

"""
This module contains a class `Rectangle` that defines a rectangle
"""


class Rectangle:
    """
    A class used to represent a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initalizes `Rectangle`"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """string represenation of an instance of `Rectangle`"""
        if self.width == 0 or self.height == 0:
            return ''
        rectangle_str = ''
        for i in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rectangle_str += '\n'

        return rectangle_str

    def __repr__(self):
        """returns detailed info about an object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """alert when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares 2 rectangles based on their areas"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that basically a square"""
        return cls(size, size)
