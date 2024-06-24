from Triangle import Triangle


class Triangle_pyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h
        self.dim = 3

    def dimention(self):
        return self.dim

    def squareSurface(self):
        l = (self.h ** 2 + (self.a / 2) ** 2) ** 0.5
        Pyramid_side = self.a * l / 2
        Pyramid_base = super().square()
        Pyramid_total = Pyramid_base + 3 * Pyramid_side
        return Pyramid_total

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        V = self.squareBase() * self.h / 3
        return V


if __name__ == '__main__':
    t = Triangle_pyramid(6, 3)
    print(t.square())
    print(t.dimention())
    print(t.perimetr())
    print(t.volume())
