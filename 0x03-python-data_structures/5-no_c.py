#!/usr/bin/python3
def no_c(my_string):
    return "".join(lt for lt in my_string if lt not in "cC")
