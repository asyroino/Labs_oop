class Equation:
    INF = "infinity"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.b}x + {self.c} = 0"

    def show(self):
        print(self)

    def solve(self):
        if self.b == 0:
            if self.c != 0:
                return ()
            else:
                return Equation.INF

        else:
            x = -self.c / self.b
            return (x,)


if __name__ == '__main__':
    e1 = Equation(2, 3)
    print(e1)
    e1.show()
    print(e1.solve())

    e2 = Equation(0, 3)
    print(e2)
    e2.show()
    print(e2.solve())

    e3 = Equation(2, 0)
    print(e3)
    e3.show()
    print(e3.solve())

    e4 = Equation(0, 0)
    print(e4)
    e4.show()
    print(e4.solve())
