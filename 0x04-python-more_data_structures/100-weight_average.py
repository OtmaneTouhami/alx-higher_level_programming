#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    weights_sum = 0
    if my_list:
        for t in my_list:
            result += t[0] * t[1]
            weights_sum += t[1]
        result /= weights_sum

    return result
