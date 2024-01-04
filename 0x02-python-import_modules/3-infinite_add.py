#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    number_of_arguments = len(argv)
    sum = 0
    for i in range(1, number_of_arguments):
        sum += int(argv[i])
    print(sum)
