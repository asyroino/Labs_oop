from Triangle import Triangle


class Rectangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a, b,
                         (a ** 2 + b ** 2) ** 0.5)

    def square(self):
        return 2 * super().square()

    def perimetr(self):
        P = 2 * (self.a + self.b)
        return P

    def __str__(self):
        return f"Trapeze: a={self.a}, b={self.b}"


if __name__ == '__main__':
    t = Rectangle(2, 5)
    print(t.square())
    print(t.dimention())
    print(t.perimetr())
    print(t.volume())
