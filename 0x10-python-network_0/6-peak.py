#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""

    x = list_of_integers
    if (len(x) == 0):
        return "None"
    i = len(x)-1
    a = 0
    while i + 1:
        if x[i] >= x[i - 1]:
            if x[i] >= a:
                a = x[i]
        else:
            if x[i - 1] >= a:
                a = x[i - 1]
        i = i-1
    return (a)
