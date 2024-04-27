#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    x = list_of_integers
    left = 0
    right = len(x) - 1

    if (len(x) == 0):
        return "None"
    while left < right:
        m = (left + right) // 2
        if x[m] < x[m + 1]:
            left = m + 1
        else:
            right = m
    return (x[left])
