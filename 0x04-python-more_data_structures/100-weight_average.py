#!/usr/bin/python3
def weight_average(my_list=[]):
    # result = 0
    # weights_sum = 0
    if my_list:
        # for a, b in my_list:
        #     result += a * b
        #     weights_sum += b
        # result /= weights_sum
        return sum(a * b for a, b in my_list) / sum(b for a, b in my_list)
    # return result
    return 0
