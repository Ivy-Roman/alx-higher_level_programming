#!/usr/bin/python3

"""
Module - 1-my_list
"""


class MyList(list):
    """
    class inherits from list

    Method
    print_sorted(self)

    """
    def print_sorted(self):
        """prints lists of integers in ascending order"""
        print(sorted(self))
