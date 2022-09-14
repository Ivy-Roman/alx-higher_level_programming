#!/usr/bin/python3

"""
module - 2-squate.py
defined a class that defines a square
"""


class Square:
    """
    class Square defined

    Args:
        size (int): size of a size in square
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            __size (int): size of a side of suare, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
