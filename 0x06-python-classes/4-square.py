#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    def __init__(self, size=0):
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return self.__size**2
    
    @property
    def size(self):
        return __size
    
    @size.setter
    def size(self, value):
        if(type(value) != int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value