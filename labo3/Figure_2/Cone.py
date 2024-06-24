from Circle import Circle


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
        self.dim = 3

    def dimention(self):
        return self.dim

    def squareSurface(self):
        l = (self.h ** 2 + self.r ** 2) ** 0.5
        Area = super().perimetr() * (self.r + l) / 2
        return Area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        V = super().square() * self.h / 3
        return V
