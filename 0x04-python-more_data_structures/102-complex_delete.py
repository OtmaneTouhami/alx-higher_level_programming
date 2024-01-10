#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value):
    return {k: v for k, v in a_dictionary.items() if v != value}
