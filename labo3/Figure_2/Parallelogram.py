from Figure import Figure


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        self.dim = 2

    def dimention(self):
        return self.dim

    def square(self):
        S = self.a * self.h / 2

    def perimetr(self):
        P = 2 * (self.a + self.b)
        return P

    def __str__(self):
        return f"Parallelogram: a={self.a}, b={self.b}, h={self.h}"
