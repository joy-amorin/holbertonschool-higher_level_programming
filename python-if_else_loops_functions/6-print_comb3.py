#!/usr/bin/python3

c = 0

for i in range(8):
    c += 1
    for j in range(10):
        if i != j and i < j:
            print("{}{}".format(i, j), end=", ", sep="")
print("{}".format(89))
