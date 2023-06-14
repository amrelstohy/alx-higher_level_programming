#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x == 8 and y == 9:
            print("{:01d}{}".format(x, y),)
            break
        if y <= x:
            continue
        print("{:01d}{}, ".format(x, y), end='')
