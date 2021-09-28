#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    "A sqaure class that accepts int positive variable size"
    def __init__(self, size=0):
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        "Calculates the area of the square"
        return self.__size**2
