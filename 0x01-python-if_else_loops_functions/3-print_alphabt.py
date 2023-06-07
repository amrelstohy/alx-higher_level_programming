#!/usr/bin/python3
for loop in list(map(chr, range(97, 123))):
    if loop != 'e' and loop != 'q':
        print("{}".format(loop), end="")
