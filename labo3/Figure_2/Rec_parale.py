from Rectangle import Rectangle


class Rec_parale(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
        self.dim = 3

    def dimention(self):
        return self.dim

    def squareSurface(self):
        Area = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        return Area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        V = self.a * self.b * self.c
        return V
