#!/usr/bin/python3

def uniq_add(my_list=[]):
    l_uniq_number = []
    _sum = 0
    uniq_number = set(my_list)
    for i in uniq_number:
        l_uniq_number.append(i)
    for n in range(len(l_uniq_number)):
        _sum += l_uniq_number[n]
    return _sum
