#!/usr/bin/python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle
import os


class CustomObject:
    """Custom class with serialization and deserialization methods."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to the specified file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an instance from the specified file."""
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        return None
