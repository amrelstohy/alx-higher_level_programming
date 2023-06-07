#!/usr/bin/python3

def upper(c):
    asci = ord(c)
    if asci >= 97 and asci <= 127:
        return (chr(65 + (asci - 97)))
    else:
        return(c)


def uppercase(str):
    for loop in str:
        print("{}".format(upper(loop)), end="")
    print("")
