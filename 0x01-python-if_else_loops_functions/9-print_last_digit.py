#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        r = ((-1 * number) % 10)
    else:
        r = number % 10
    print("{}".format(r), end="")
    return (r)
