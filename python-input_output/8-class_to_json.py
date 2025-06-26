#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
description of an object for JSON serialization.
"""

def class_to_json(obj):
    """Returns the dictionary description of obj for JSON serialization."""
    return obj.__dict__
