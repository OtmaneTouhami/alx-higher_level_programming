#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
       }
    result = 0
    current_roman = 0

    for letter in roman_string[::-1]:
        value = roman_int.get(letter)
        if value >= current_roman:
            result += value
        else:
            result -= value
        current_roman = value

    return result
