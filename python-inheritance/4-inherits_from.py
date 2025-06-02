#!/usr/bin/python3
"""
check if object inherits from class
"""

def inherits_from(obj, a_class):
    """
    return true if obj inherits from a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
