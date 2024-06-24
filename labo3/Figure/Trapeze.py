from Triangle import Triangle
import turtle as t


class Trapeze(Triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x3, y3)
        self.vertex3 = x2, y2

    def get_square(self):
        S_triangle = super().get_square()
        h = 2 * S_triangle / self.get_side_len(self.start, self.vertex2)
        middle_line = (self.get_side_len(self.vertex1, self.vertex3) + self.get_side_len(self.start, self.vertex2)) / 2
        S_trapeze = h * middle_line
        return S_trapeze

    def get_perimetr(self):
        AB = self.get_side_len(self.start, self.vertex1)
        AD = self.get_side_len(self.start, self.vertex3)
        BC = self.get_side_len(self.vertex1, self.vertex3)
        CD = self.get_side_len(self.vertex3, self.vertex2)

        P = AB + AD + BC + CD

        return P

    def draw(self):
        v2 = self.vertex1
        v3 = self.vertex3
        v4 = self.vertex2

        self._draw_vertex(v2, v3, v4)


if __name__ == '__main__':
    t1 = Trapeze(20, 50, 80, 50, 100, 0)
    t1.draw()
    print(t1.get_square())
    print(t1.get_perimetr())
    t.mainloop()
