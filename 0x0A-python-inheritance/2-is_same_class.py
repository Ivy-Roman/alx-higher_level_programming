#!/usr/bin/python3

"""
module - 2-is_same_class
A function that returns True if the object is exactly an instance
of the specified class; otherwise False

"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Return:
        True if the object is an instance of class, else false.
    """
    return type(obj) = a_class
