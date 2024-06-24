class Trapeze:

    def __init__(self, a, b, c ,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):
        P = self.a + self.b + self.c + self.d
        return P

    def exist(self):
        p = (self.c + self.d + self.a - self.b) / 2
        triangle_inside_area = p * (p - self.c) * (p - self.d) * (p - self.a + self.b)

        if triangle_inside_area > 0:
            return True
        else:
            return False

    def area(self):
        p = (self.c + self.d + self.a - self.b) / 2
        triangle_inside_area = p * (p - self.c) * (p - self.d) * (p - self.a + self.b)

        h = 2 * (triangle_inside_area ** 0.5 ) / (self.a - self.b)
        middle_line = (self.a + self.b) / 2

        area = h * middle_line
        return abs(area)


if __name__ == "__main__":
    obj = Trapeze(6, 11, 9, 4)
    if obj.exist():
        print(obj.perimetr())
        print(obj.area())