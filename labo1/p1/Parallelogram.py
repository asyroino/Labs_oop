class Parallelogram():
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def exist(self):
        if self.a > 0 and self.b > 0 and self.h > 0:
            return True
        else:
            return False

    def perimetr(self):
        P = (self.a + self.b) * 2
        return P

    def area(self):
        area = self.b * self.h

        return area