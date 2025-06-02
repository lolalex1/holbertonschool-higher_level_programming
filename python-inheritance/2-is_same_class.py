#!/usr/bin/python3
"""
check if object is exact instance of class
"""

def is_same_class(obj, a_class):
    """
    return true if obj is exact instance of a_class
    """
    return type(obj) is a_class