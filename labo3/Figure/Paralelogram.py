from Triangle import Triangle
import turtle as t


class Paralelogram(Triangle):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def get_square(self):
        S = super().get_square()
        return 2 * S

    def get_perimetr(self):
        P = super().get_perimetr() - self.get_side_len(self.vertex2, self.vertex1)
        return 2 * P

    def draw(self):
        v2 = self.vertex1
        v3 = (self.vertex1[0] + self.vertex2[0], self.vertex1[1] + self.vertex2[1])
        v4 = self.vertex2
        self._draw_vertex(v2, v3, v4)


if __name__ == '__main__':
    t1 = Paralelogram(20, 70, 100, 10)
    print(t1.get_square())
    print(t1.get_perimetr())
    t1.draw()
    t.mainloop()
