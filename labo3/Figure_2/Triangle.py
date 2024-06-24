from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and c + b > a
        self.a = a
        self.b = b
        self.c = c
        self.dim = 2

    def dimention(self):
        return self.dim

    def perimetr(self):
        P = self.a + self.b + self.c
        return P

    def square(self):
        if (self.a ** 2 + self.b ** 2) ** 0.5 == self.c:
            return self.a * self.b / 2

        else:
            p = self.perimetr() / 2
            S = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
            return S

    def __str__(self):
        return f"Triangle: a={self.a}, b={self.b}, c={self.c}"


if __name__ == '__main__':
    t = Triangle(1, 4, 5)
    print(t.square())
    print(t.dimention())
    print(t.perimetr())
    print(t.volume())
