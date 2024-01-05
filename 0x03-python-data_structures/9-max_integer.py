#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    if len(my_list) != 0:
        max = my_list[0]
        for number in my_list:
            max = number if number > max else max
    return max
