#!/usr/bin/python3
"""
This module provides a function to append a string to the end
of a UTF-8 text file and return the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends text to a UTF-8 file and returns the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
