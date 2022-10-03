#!/usr/bin/python3
"""
Module 4-inherits_from.py
returns True if obj is instance of class that it inherits from or
is a subclass of

"""


def inherits_from(obj, a_class):
    """
    Return:
        True if object is instance of class that it inherits
        from or is a subclass of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
