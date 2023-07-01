#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    b = []
    c = []
    for x in range(0, 2):
        if len(tuple_a) <= x:
            a.append(0)
        else:
            a.append(tuple_a[x])
        if len(tuple_b) <= x:
            b.append(0)
        else:
            b.append(tuple_b[x])
        c.append(a[x]+b[x])
    return ((c[0], c[1]))
