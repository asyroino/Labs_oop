class Figure:

    def dimention(self):
        return None

    def perimetr(self):
        assert self.dimention() == 2
        return None

    def square(self):
        assert self.dimention() == 2
        return None

    def squareSurface(self):
        assert self.dimention() == 3
        return None

    def squareBase(self):
        assert self.dimention() == 3
        return None

    def height(self):
        assert self.dimention() == 3

    def volume(self):
        if self.dimention() == 2:
            return self.square()
