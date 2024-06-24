from Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r):
        assert r > 0
        self.r = r
        self.dim = 2

    def square(self):
        return pi * self.r ** 2

    def perimetr(self):
        super().perimetr()
        return 2 * pi * self.r

    def dimention(self):
        self.dim = 2

    def __str__(self):
        return f"Circle: r={self.r}"
