#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key=""):
    if key and a_dictionary.get(key):
        a_dictionary.pop(key)
    return a_dictionary
