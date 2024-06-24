from Rational import Rational
from copy import copy
from RationalListIterator import RationalListIterator


class RationalList:
    def __init__(self, rational_arr):
        # self.check_condition(rational_arr)
        self.rational_arr = rational_arr

    # region static_methods
    @staticmethod
    def check_condition(rational_arr):
        if len(rational_arr) == 0:
            return
        else:
            for rational in rational_arr:
                assert type(rational) == Rational, "Усі числа списку повинні бути об'єктами класу Rational"


    def sum(self):
        zero = Rational(0)
        for number in self.rational_arr:
            zero = zero + number

        return zero


    def __str__(self):
        s = "Rational_arr: "

        for rational in self.rational_arr:
            s += f"{rational}, "

        return s[:len(s) - 2]

    def __len__(self):
        return len(self.rational_arr)

    def __getitem__(self, index):
        assert type(index) == int, "Допускається лише Integer"

        return self.rational_arr[index]

    def __setitem__(self, index, value):
        new_arr = copy(self.rational_arr)

        if index < len(self.rational_arr):
            new_arr[index] = value

        elif index == len(self.rational_arr):
            new_arr.append(value)

        else:
            raise IndexError

        return RationalList(new_arr)

    def __add__(self, other):
        new_arr = copy(self.rational_arr)

        if type(other) == RationalList:
            new_arr.extend(other.rational_arr)

        elif type(other) == Rational or type(other) == int:
            new_arr.append(other)

        else:
            raise ValueError

        return RationalList(new_arr)

    def __iadd__(self, other):
        if type(other) == RationalList:
            self.rational_arr.extend(other.rational_arr)

        elif type(other) == Rational or type(other) == int:
            self.rational_arr.append(other)

        else:
            raise ValueError

        return self

    def __iter__(self):
        return RationalListIterator(self.rational_arr)


if __name__ == '__main__':
    r1 = (Rational(5))
    r2 = (Rational(6))
    r3 = (Rational(7))
    r4 = (Rational(8))
    r5 = Rational(3, 4)
    r6 = Rational(7, 8)
    arr = [r1, r2, r3, r5, r6, r4]
    arr = RationalList(arr)
    print(arr)
