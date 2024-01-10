#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict) -> dict:
    result: dict = dict()
    for key, value in a_dictionary.items():
        result[key] = value * 2
    return result
