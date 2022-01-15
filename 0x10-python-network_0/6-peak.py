#!/usr/bin/python3
"""
This module calculates the peak in an array of numbers
"""


def find_peak(list_of_integers):
    """
    This finds the peak from the array
    """
    if(list_of_integers):
        arr_len = len(list_of_integers)
        list_of_integers.sort()
        return list_of_integers[arr_len - 1]
