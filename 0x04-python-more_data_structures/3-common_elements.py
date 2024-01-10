#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = set()
    for elm_1 in set_1:
        for elm_2 in set_2:
            if elm_1 == elm_2:
                res.add(elm_2)
    return res
