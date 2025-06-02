#!/usr/bin/python3
"""
square class inherits from rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    square with size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
