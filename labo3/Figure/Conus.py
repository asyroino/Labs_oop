from Circle import Circle
import turtle as t


class Conus(Circle):
    def __init__(self, r, h, x=0, y=0):
        super().__init__(r, x, y)
        self.height = h
        self._dimention = 3

    def get_squareBase(self):
        return super().get_square()

    def get_squareSurface(self):
        surface = super().get_perimetr() / 2 * (self.r ** 2 + self.height ** 2) ** 0.5
        return surface

    def figure_vol(self):
        V = super().get_square() * self.height / 3
        return V

    def get_height(self):
        return self.height

    def draw(self):
        super().draw()
        t.up()
        vertex = self.start[0], self.start[1] + self.height + self.r
        t.setpos(self.start[0] - self.r, self.start[1])
        t.down()
        t.goto(*vertex)
        t.goto(self.start[0] + self.r, self.start[1])
        t.up()


if __name__ == '__main__':
    c = Conus(50, 200)
    c.draw()
    t.mainloop()
