from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c}"

    def show(self):
        print(self)

    def solve(self):
        set_of_solutions = set()
        possible_quadratic_solutions = super().solve()

        if isinstance(possible_quadratic_solutions, tuple):
            for solution in possible_quadratic_solutions:
                if solution >= 0:
                    t1 = solution ** 0.5
                    t2 = -solution ** 0.5
                    set_of_solutions.add(t1)
                    set_of_solutions.add(t2)

            return tuple(set_of_solutions)

        else:
            return self.INF


if __name__ == '__main__':
    e = BiQuadraticEquation(0, 5, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 0, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 0, 0)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 5, 0)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, 3, 8)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, 4, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, -3, 2)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(2, -6, 4)
    print(e)
    print(e.solve())
