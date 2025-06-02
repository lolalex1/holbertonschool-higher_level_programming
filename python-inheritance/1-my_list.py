#!/usr/bin/python3
"""
class that inherits from list
"""


class MyList(list):
    """
    prints the list sorted
    """

    def print_sorted(self):
        print(sorted(list(self)))
