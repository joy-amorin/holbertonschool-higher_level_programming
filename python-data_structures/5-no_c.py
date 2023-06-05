#!/usr/bin/python3

def no_c(my_string):

    str_c = ""
    for i in my_string:
        if i != "c" and i != "C":
            str_c += i
    return str_c
