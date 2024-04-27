#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""

    x = list_of_integers
    if (len(x) == 0):
        return "None"
    return (max(x))
