#!/usr/bin/python3

"""
module - 1-square.py
defines class Square with private attribute size
"""


class Square:
    """
    class Square defined

    Args:
        size: size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: size of a side of a square
        """
        self.__size = size
