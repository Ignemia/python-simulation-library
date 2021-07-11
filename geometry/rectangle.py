from geometry.shape2d import Shape2D
from geometry.vector2d import Vector2D
from geometry.vertex import Vertex


class Rectangle(Shape2D):
    def __init__(self, center, sides):
        Shape2D.__init__(self)

        vertex = Vertex((center.get_normal_x(), center.get_normal_y()))

        self.set_relative_object(vertex)

        x_pos = self.get_x() + sides[0]
        y_pos = self.get_y() + sides[1]
        x_neg = self.get_x() - sides[0]
        y_neg = self.get_y() - sides[1]

        self.vertices = [
            Vertex((x_neg, y_neg)),
            Vertex((x_neg, y_pos)),
            Vertex((x_pos, y_pos)),
            Vertex((x_pos, y_neg))
        ]

        self.vectors = [
            Vector2D(vertex, self.vertices[0]),
            Vector2D(vertex, self.vertices[1]),
            Vector2D(vertex, self.vertices[2]),
            Vector2D(vertex, self.vertices[3])
        ]


    def rotate(self, angle):
        self.current_rotation += angle
        self.vectors[0].rotate(angle)
        self.vectors[1].rotate(angle)
        self.vectors[2].rotate(angle)
        self.vectors[3].rotate(angle)

        self.vertices[0].set_position(self.vectors[0].get_endpoint())
        self.vertices[1].set_position(self.vectors[1].get_endpoint())
        self.vertices[2].set_position(self.vectors[2].get_endpoint())
        self.vertices[3].set_position(self.vectors[3].get_endpoint())

        return self
