from Triangle import Triangle
import turtle as t


class Rectangle(Triangle):
    def __init__(self, x, y):
        super().__init__(0, y, x, 0)
        self.vertex3 = (x, y)

    def get_square(self) -> float:
        s_triangle = super().get_square()
        S = 2 * s_triangle
        return S

    def get_perimetr(self) -> float:
        """
        p_triangle - периметр трикутника, сторони якого - дві сторони прямокутника + діагональ
        p_rectangle: віднімаємо в p_triangle діагональ
        :return: повертаємо p_rectangle помножений на 2
        """
        p_triangle = super().get_perimetr()
        P_rectagnle = p_triangle - self.get_side_len(self.vertex1, self.vertex2)
        P_rectagnle = 2 * P_rectagnle
        return P_rectagnle

    def draw(self):
        v2 = self.vertex1
        v3 = self.vertex3
        v4 = self.vertex2
        self._draw_vertex(v2, v3, v4)


if __name__ == '__main__':
    t1 = Rectangle(50, 50)
    print(t1.get_perimetr())
    print(t1.get_square())
    t1.set_start(1, 1)
    t1.draw()
    t1.rotation_angel = 30
    t1.draw()
    t1.scale_coords = (2, 2)
    t1.draw()
    t.mainloop()
