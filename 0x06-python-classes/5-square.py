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
        "Calculates the area of the square and returns the value"
        return self.__size**2
    
    @property
    def size(self):
        "returns the value of size"
        return self.__size
    
    @size.setter
    def size(self, value):
        "sets the value of size"
        if(type(value) != int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def my_print(self):
        "This prints the square on the terminal"
        if(self.__size > 0):
            [print("#" * self.__size) for i in range(int(self.__size))]
        else:
            print()
