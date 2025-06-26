#!/usr/bin/python3
"""
This module provides a function to write a Python object
to a text file using its JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """Writes a Python object to a file in JSON format."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
