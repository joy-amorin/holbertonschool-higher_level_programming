#!/usr/bin/python3

def multiple_returns(sentence):
    len_s = len(sentence)
    c = None
    if sentence != "":
        c = sentence[0]
    return len_s, c
