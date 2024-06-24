from Triangle import Triangle
import turtle as t


class TriangularPiramid(Triangle):
    def __init__(self, x, y, h):
        super().__init__(x, y, *self._calc_another_vertex(x, y))
        self.height = h
        self._dimention = 3
        self.vertex3 = self._calc_height_center()

    def _calc_another_vertex(self, x, y):
        self.rotation_angel = 60
        rotated_x, rotated_y = self.rotation_calc(x, y)
        self.rotation_angel = 0
        return rotated_x, rotated_y

    def _calc_height_center(self):
        x = (self.start[0] + self.vertex1[0] + self.vertex2[0]) / 3
        y = (self.start[1] + self.vertex1[1] + self.vertex2[1]) / 3
        return x, y + self.height

    def get_squareSurface(self):
        return super().get_perimetr() * self.height / 2

    def get_squareBase(self):
        return super().get_square()

    def figure_vol(self):
        return super().get_square() * self.height / 3

    def draw(self):
        super().draw()
        v1, v2, v3 = self.start, self._calc_vertex(self.vertex1), self._calc_vertex(self.vertex2)
        self.set_start(self.start[0], self.start[1] + self.height)
        d = self.vertex3
        arr = [(v1, d), (v2, d), (v3, d)]
        for v, n in arr:
            t.up()
            t.setpos(*v)
            t.down()
            t.goto(*n)


if __name__ == '__main__':
    c1 = TriangularPiramid(20, 80, 100)
    t.speed(0)
    c1.draw()
    print(c1.get_squareSurface())
    print(c1.get_volume())
    print(c1.get_height())
    print(c1.get_square())
    print()
    print()
    print()
    print()
    t.mainloop()
