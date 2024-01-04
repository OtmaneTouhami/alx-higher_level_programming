#!/usr/bin/python3
from calculator_1 import add, div, mul, sub
from sys import argv, exit
if __name__ == '__main__':
    arguments_number = len(argv) - 1
    if arguments_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ('-', '/', '*', '+'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        else:
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
