#!/usr/bin/python3
"""
This module defines a Student class with attributes and
a method to convert its instance to a dictionary.
"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the Student instance."""
        return self.__dict__
