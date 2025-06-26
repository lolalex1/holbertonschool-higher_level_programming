#!/usr/bin/python3
"""
This module defines a Student class that supports serialization
and deserialization to and from JSON-compatible dictionary structures.
"""

class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are included.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using key-value pairs from the given dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
