class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):

        P = self.a + self.b + self.c
        return P

    def exist(self):
        first = self.a + self.b > self.c
        second = self.c + self.b > self.a
        third = self.c + self.a > self.b

        if first and second and third:
            return True
        else:
            return False

    def area(self):
        P = self.perimetr()
        p = P / 2
        area = (p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5
        return area


if __name__ == "__main__":
    t = Triangle(4, 3, 5)
    print(t.exist())
    print(t.perimetr())
    print(t.area())