#!/usr/bin/python3

"""
module - 6-square.py
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
        position(self)
        position(self, value)
        area(self)
        print(self)
    """

    def __init__(self, size=0):
        """
        Initialises square

        Attributes:
            __size (int): defaults to 0 if none
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        Return position
        """

    @property
    def position(self, value):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
