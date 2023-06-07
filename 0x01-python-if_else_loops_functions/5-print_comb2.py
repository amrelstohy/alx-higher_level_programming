#!/usr/bin/python3
for loop in range(100):
    if loop == 99:
        print("{}".format(loop))
    else:
        print("{num:02d},".format(num=loop), end=" ")
