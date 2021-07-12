from geometry.shape2d import Shape2D
from geometry.vertex import Vertex


class Ellipse(Shape2D):
    def __init__(self, center, radii):
        Shape2D.__init__(self)
        vertex = Vertex((center.get_x(), center.get_y()))
        self.radii = radii
        self.set_relative_object(vertex)

    def rotate(self, angle):
        self.current_rotation += angle

        return self
