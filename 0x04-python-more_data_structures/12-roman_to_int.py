#!/usr/bin/python3
def roman_to_int(roman_string: str):
    roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    current_roman = 0
    if type(roman_string) is str and roman_string is not None:         
        for letter in roman_string[::-1]:
            if roman_int.get(letter) >= current_roman:
                result += roman_int.get(letter)
            else:
                result -= roman_int.get(letter)
            current_roman = roman_int.get(letter)
        return result
    return 0
