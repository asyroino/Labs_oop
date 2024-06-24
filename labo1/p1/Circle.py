class Circle:
    pi = 3.14159265359
    def __init__(self, r):
        self.r = r

    def exist(self):
        if self.r > 0:
            return True
        else:
            return False

    def perimetr(self):
        p = 2 * self.pi * self.r
        return p

    def area(self):
        area = self.pi * self.r ** 2
        return area


if __name__ == "__main__":
    circle1 = Circle(1)
    print(circle1.__class__.__name__)
    print(circle1.perimetr())
    print(circle1.area())