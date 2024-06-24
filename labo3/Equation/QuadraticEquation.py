from Equation import Equation


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        super().__init__(b, c)

    def __str__(self):
        return f"{self.a}x^2 + {super().__str__()}"

    def get_discriminant(self):
        D = self.b ** 2 - 4 * self.a * self.c
        return D

    def solve(self):
        if self.a == 0:
            return super().solve()

        D = self.get_discriminant()

        if D > 0:
            D_sqrt = D ** 0.5
            x1 = (-self.b + D_sqrt) / (2 * self.a)
            x2 = (-self.b - D_sqrt) / (2 * self.a)
            return x1, x2

        elif D == 0:
            x = -self.b / (2 * self.a)
            return (x,)

        else:
            return ()


if __name__ == '__main__':
    q1 = QuadraticEquation(2, 3, 0)
    q2 = QuadraticEquation(0, 3, 1)
    q3 = QuadraticEquation(2, 0, -1)
    q4 = QuadraticEquation(0, 0, 1)
    equations = (q1, q2, q3, q4)

    for obj in equations:
        print(obj)
        obj.show()
        print(obj.solve())
