import math

from geometry.ellipse import Ellipse
from geometry.shape2d import Shape2D


class Circle(Shape2D, Ellipse):
    def __init__(self, center, radius):
        Shape2D.__init__(self)
        self.set_attribute("position", center)
        self.radius = radius
        self.area = math.pi * self.radius ** 2
