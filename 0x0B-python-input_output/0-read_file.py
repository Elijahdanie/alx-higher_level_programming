#!/usr/bin/python3
"""This module defines the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
    filename (str): Filename

    >>> read_file('0-read_file.py')
    """
    with open(filename, encoding='utf-8') as file:
        [print(line, end="") for line in file]
