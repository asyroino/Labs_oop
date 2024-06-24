from Figure import Figure
from math import pi
import turtle as t


class Circle(Figure):
    def __init__(self, r, x=0, y=0):
        super().__init__()
        self.r = r
        self.start = (x, y)

    def get_square(self):
        S = pi * self.r ** 2
        return S

    def get_perimetr(self):
        P = 2 * pi * self.r

    def draw(self):
        start = (self.start[0], self.start[1] - self.r)
        t.up()
        t.setpos(*start)
        t.down()
        t.circle(self.r)


if __name__ == '__main__':
    c = Circle(50)
    c.draw()
