#!/usr/bin/python3
def best_score(a_dictionary: dict) -> str:
    if a_dictionary:
        key, max_value = list(a_dictionary.items())[0]
        for k, v in a_dictionary.items():
            if v > max_value:
                key, max_value = k, v
        return key

    return None
