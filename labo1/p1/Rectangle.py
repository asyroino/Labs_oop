class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def exist(self):
        if self.a * self.b > 0:
            return True
        else:
            return False

    def perimetr(self):
        P = (self.a + self.b) * 2
        return P

    def area(self):
        area = self.a * self.b
        return area