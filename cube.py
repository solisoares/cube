import os

from math import cos, sin, pi, floor
from time import sleep
from numpy import arange

from typing import List


def clear_terminal():
    os.system('clear')


class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def translate_on_x_axis(self, alpha):
        pass

    def translate_on_y_axis(self, alpha):
        pass

    def translate_on_z_axis(self, alpha):
        """Rotate Point around the z axis by an specified amount

        The z coordinate doesn't change
        """
        x = self.x*cos(alpha) - self.y*sin(alpha)
        y = self.x*sin(alpha) + self.y*cos(alpha)
        self.x, self.y = x, y


class Square:
    def __init__(self, *vertices: Point) -> None:
        """_summary_
                               z
        z2 --> v4 ___ v3       |   y
               |       |       |  / 
               |       |       | /
        z1 --> v1 ___ v2       |/______ x
               ^       ^
               |       |
               x1      x2
        """
        self.v1, self.v2, self.v3, self.v4 = self.vertices = vertices

    def translate_on_z_axis(self, alpha):
        for vertice in self.vertices:
            vertice.translate_on_z_axis(alpha)

    def ascii(self, x_offset=50, z_offset=5, art='.'):
        x1, x2 = self.v1.x, self.v2.x
        z1, z2 = self.v1.z, self.v4.z
        dx = floor(x2 - x1)
        dz = floor(z2 - z1)
        single_line = art*(abs(dx)+1)
        print("\n"*z_offset)
        for i in range(dz):
            if dx > 0:
                print(' '*(x_offset+floor(x1)) + single_line)
            else:
                print(' '*(x_offset - floor(abs(x2))-1) + single_line)
        # print(f"{dx=}")
        # print(f"{dz=}")


square = Square(
    Point(25, 0, 0), Point(35, 0, 0),
    Point(25, 0, 5), Point(35, 0, 5)
)


while True:
    alpha = 0.1
    for _ in arange(0, 2*pi, alpha):
        square.translate_on_z_axis(alpha)
        square.ascii()
        sleep(0.025)
        clear_terminal()
