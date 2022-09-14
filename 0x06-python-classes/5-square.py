#!/usr/bin/python3

"""
module - 5-square.py
defined class Square with setter and getter that returns square area
can print the square to stdout sing #
"""


class Square:
    """
    Defined class Square

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        print(self)
    """

    def __init__(self, size=0):
        """
        Initialises square

        Attributes:
            __size (int): defaults to 0 if none
        """
        self.size = size

    @property
    def size(self):
        """
        getter

        returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter

        args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculates current area of square

        returns area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints the square with #
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
