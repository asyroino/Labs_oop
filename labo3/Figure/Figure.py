from math import sin, cos, radians
from random import randint as rand


class Figure:
    default_color = '#000000'

    def __init__(self):
        self.color = Figure.default_color
        self.rotation_angel = 0
        self.scale_coords = (1, 1)
        self.start = (0, 0)
        self._dimention = 2

    # region setters

    def set_start(self, x, y):
        self.start = (x, y)

    def set_color(self, color):
        assert self.is_color_exist(color)
        self.color = color

    def set_rotation_angle(self, fi):
        self.rotation_angel = fi

    def set_scale(self, scale_x, scale_y):
        self.scale_coords = scale_x, scale_y

    # endregion

    def get_dimention(self):
        return self._dimention

    def get_perimetr(self):
        assert self._dimention == 2

    def get_square(self):
        assert self._dimention == 2

    def get_squareSurface(self):
        assert self._dimention != 2

    def get_squareBase(self):
        assert self._dimention != 2

    def get_height(self):
        assert self._dimention != 2

    def figure_vol(self):
        assert self._dimention == 2

    def get_volume(self):
        if self._dimention == 2:
            return self.get_square()
        else:
            return self.figure_vol()

    # region staticmethods

    @staticmethod
    def is_color_exist(color_code: str) -> bool:
        """
        :param color_code: string
        :return: True, if color exsists, else - False
        """
        if not (color_code.startswith('#') and len(color_code) == 7):
            return False

        for char in color_code[1:]:
            if not (char.isdigit() or char.lower() in 'abcdef'):
                return False

        return True

    @staticmethod
    def random_angle() -> int:
        """
        :return: random integer from [a;b]
        """
        return rand(1, 360)

    @staticmethod
    def set_random_color() -> str:
        """
        :return: random RGB code
        """
        R = rand(0, 255)
        G = rand(0, 255)
        B = rand(0, 255)

        return f'#{R:02X}{G:02X}{B:02X}'

    # endregion

    # region main_funcs
    def calc_vertex(self, x, y):
        v = (self.start[0] + x,
             self.start[1] + y)
        return v

    def rotation_calc(self, x, y) -> tuple:
        """
        :param x: OX coord
        :param y: OY coord
        :return: rotated x,y which had multiplied by rotation matrix
        """
        fi = radians(self.rotation_angel)
        rotated_x = x * cos(fi) - y * sin(fi)
        rotated_y = x * sin(fi) + y * cos(fi)

        return rotated_x, rotated_y

    def scale_vertex(self, x, y) -> tuple:
        """
        :param x: x coord
        :param y: y coord
        :return: x,y which scalar multiplied by self.scale
        """
        scaled_x = x * self.scale_coords[0]
        scaled_y = y * self.scale_coords[1]
        return scaled_x, scaled_y
    # endregion
