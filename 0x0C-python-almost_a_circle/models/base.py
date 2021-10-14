#!/usr/bin/python3
"""
This module represents the base class for all 
subsequent classes in this package
"""

class Base:
    """
    This class represents the base for subsequent classes
    in this project

    Attributes:
     __nb_objects: this represents the unique object id

    >>> b1 = Base()
    >>> print(b1.id)
    1
    >>> b2 = Base()
    >>> print(b2.id)
    2
    >>> b3 = Base()
    >>> print(b3.id)
    3
    >>> b4 = Base(12)
    >>> print(b4.id)
    12
    >>> b5 = Base()
    >>> print(b5.id)
    4
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is called when a new instance of Base is created
            Args:
                id : is used to manage attributes and aboid creating same code
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
