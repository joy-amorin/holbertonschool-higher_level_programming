#!/usr/bin/python3

def best_score(a_dictionary):
    num = 0
    best_key = None
    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if value > num:
            num = value
            best_key = key
    return best_key
