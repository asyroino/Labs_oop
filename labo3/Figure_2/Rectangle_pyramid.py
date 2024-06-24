from Rectangle import Rectangle


class Rectangle_pyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
        self.dim = 3

    def dimention(self):
        return self.dim

    def squareSurface(self):
        a_l = ((self.a / 2) ** 2 + self.h ** 2) ** 0.5
        a_side = self.a * a_l
        a_b = ((self.b / 2) ** 2 + self.h ** 2) ** 0.5
        b_side = self.b * a_b
        base_side = super().square()
        Area = b_side + a_side + base_side
        return Area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        V = self.squareBase() * self.h / 3
        return V
