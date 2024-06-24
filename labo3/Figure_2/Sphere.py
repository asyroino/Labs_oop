from Circle import Circle
from Figure import Figure


class Sphere(Figure):
    def __init__(self, r):
        self.r = r
        self.circle = Circle(r)
        self.dim = 3

    def volume(self):
        V = self.circle.square() * self.r * (4 / 3)
        return V

    def squareBase(self):
        return self.circle.square()

    def dimention(self):
        return self.dim

    def height(self):
        return 2 * self.r

    def squareSurface(self):
        return self.circle.perimetr() * self.r * 2

    def __str__(self):
        return f"Sphere: r={self.r}"


if __name__ == '__main__':
    s = Sphere(5)
    print(s.volume())
    print(s.squareBase())
    print(s.height())
    print(s.squareBase())
