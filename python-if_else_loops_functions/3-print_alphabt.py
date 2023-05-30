#!/usr/bin/python3

for c in range(97, 123):
    if c != 113 and c != 101:
        alpha = chr(c)
        print(f"{alpha}", end="")
