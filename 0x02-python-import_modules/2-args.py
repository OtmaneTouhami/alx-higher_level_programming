#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    number_of_arguments = len(argv) - 1
    text = "argument"
    if number_of_arguments == 0 or number_of_arguments > 1:
        text += "s"
    if number_of_arguments >= 1:
        text += ":"
    elif number_of_arguments == 0:
        text += "."
    print(f'{number_of_arguments} {text}')
    for i in range(1, number_of_arguments + 1):
        print(f'{i}: {argv[i]}')
