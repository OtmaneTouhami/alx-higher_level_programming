#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        self.size = size

    def __eq__(self, other):
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
