from Triangle import Triangle


class Prizma(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h
        self.dim = 3

    def dimention(self):
        return self.dim

    def squareSurface(self):
        S_sides = self.h * super().perimetr()
        Area = 2 * super().square() + S_sides
        return Area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        V = super().square() * self.h
        return V
