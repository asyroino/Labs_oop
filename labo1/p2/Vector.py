class Vector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            vect = args[0]
            self.coords = vect.coords
        else:
            self.coords = args

    def show(self):
        return self.coords

    def dim(self):
        dim = len(self.coords)
        return dim

    def module(self):
        sum = 0
        for i in self.coords:
            sum += i**2

        return sum ** 0.5

    def average(self):
        sum = 0
        for i in self.coords:
            sum += i

        average = sum / len(self.coords)
        return average

    def min_coord(self):
        min1 = min(self.coords)
        return min1

    def max_coord(self):
        max1 = max(self.coords)
        return max1


if __name__ == "__main__":
    v = Vector(1, 2, 3)
    v.show()
    print(v.dim())
    print(v.module())
    print(v.average())
    print(v.min_coord())
    print(v.max_coord())