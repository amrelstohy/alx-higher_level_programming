#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""

    x = list_of_integers
    l, r = 0, len(x) - 1
    if (len(x) == 0):
        return "None"
    while l < r:
        m = (l + r) // 2
        if x[m] < x[m + 1]:
            l = m + 1
        else:
            r = m
    return (x[l])
