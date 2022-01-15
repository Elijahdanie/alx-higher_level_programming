#!/usr/bin/python3
"""
This module calculates the peak in an array of numbers
"""


from email.policy import strict


def find_peak(list_of_integers):
    """
    This finds the peak from the array
    """
    if len(list_of_integers) == 0:
        return None
    peak = 0
    left = 0
    right = len(list_of_integers) - 1
    iteration = len(list_of_integers)/2
    check_dec = str(iteration)
    if (len(check_dec) == 3 and check_dec[-1] == '5'):
        iteration = int(iteration) + 1
    else:
        iteration = int(iteration)
    for i in range(iteration):
        peak = isgreater(list_of_integers[left], list_of_integers[right], peak)
        right = right - 1
        left = left + 1
    return peak


def isgreater(curr, comp1, peak):
    """
    This makes comparison between values
    """
    if curr > comp1 and curr >= peak:
        return curr
    elif comp1 > curr and comp1 >= peak:
        return comp1
    elif comp1 == curr and comp1 >= peak:
        return curr
    else:
        return peak
