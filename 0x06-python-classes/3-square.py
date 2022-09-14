#!/usr/bin/python3

"""
module - 3-square.py
defined class Square that returns square area
"""


class Square:
    """
    Defined class Square

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initialises square

        Attributes:
            __size (int): size of a side of square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates current area of square

        returns area
        """
        return (self.__size)**2
