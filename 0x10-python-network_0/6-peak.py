#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    x = list_of_integers
    left = 0
    r = len(x) - 1

    if (len(x) == 0):
        return "None"
    while left < r:
        m = (left + r) // 2
        if x[m] < x[m + 1]:
            left = m + 1
        else:
            r = m
    return (x[left])
