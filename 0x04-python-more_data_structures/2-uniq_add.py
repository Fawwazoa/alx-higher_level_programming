#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    sums = 0
    new_list = set(my_list)
    for integer in new_list:
        sums = integer + sums
    return sums
