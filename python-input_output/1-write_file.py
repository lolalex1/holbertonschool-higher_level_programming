#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 text file
and return the number of characters written.
"""

def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)