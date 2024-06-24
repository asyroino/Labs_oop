from Figure import Figure


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.dim = 2

    def square(self):
        h = self.c * self.d / abs(self.a - self.b)

        S = ((self.a + self.b) / 2) * h

        return S

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def dimention(self):
        return self.dim

    def __str__(self):
        return f"Trapeze: a={self.a}, b={self.b}, c={self.c}, d={self.d}"


if __name__ == '__main__':
    t = Trapeze(6, 3, 4, 11)
    print(t.square())
    print(t.dimention())
    print(t.perimetr())
    print(t.volume())
    print(t.squareBase())
