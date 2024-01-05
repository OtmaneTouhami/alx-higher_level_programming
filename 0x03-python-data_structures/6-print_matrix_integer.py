#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for i in range(len(element)):
            print(
                "{:d}".format(element[i]),
                end=" " if i < len(element) - 1 else ""
            )
        print()
