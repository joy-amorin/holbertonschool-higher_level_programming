#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 != 0:
        alpha = chr(c - 32)
        print(alpha, end="")
    elif c % 2 == 0:
        alpha = chr(c)
        print(alpha, end="")
