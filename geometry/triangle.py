import math

from geometry.shape2d import Shape2D
from geometry.vector2d import Vector2D
from geometry.vertex import Vertex


class Triangle(Shape2D):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise TypeError(f"Triangle requires exactly 3 vertices {len(vertices)} given")
        super().__init__()

        self.vertex_a = vertices[0]
        self.vertex_b = vertices[1]
        self.vertex_c = vertices[2]

        self.centroid = self.get_centroid()
        self.position = (self.centroid.get_x(), self.centroid.get_y())

        self.vector_ab = Vector2D(self.vertex_a, self.vertex_b)
        self.vector_bc = Vector2D(self.vertex_b, self.vertex_c)
        self.vector_ca = Vector2D(self.vertex_c, self.vertex_a)

        self.circumference = self.vector_ab.get_magnitude() + self.vector_bc.get_magnitude() + self.vector_ca.get_magnitude()
        heron_s = self.circumference / 2
        heron_a = (heron_s - self.vector_ab.get_magnitude())
        heron_b = (heron_s - self.vector_bc.get_magnitude())
        heron_c = (heron_s - self.vector_ca.get_magnitude())
        self.area = math.sqrt(heron_s * heron_a * heron_b * heron_c)

    def get_centroid(self):
        return Vertex((
            (self.vertex_a.get_x() + self.vertex_b.get_x() + self.vertex_c.get_x()) / 3,
            (self.vertex_a.get_y() + self.vertex_b.get_y() + self.vertex_c.get_y()) / 3
        ))

    def move(self, amount):
        self.centroid.translate(amount)
        return self.set_attribute("position", (self.centroid.get_x(), self.centroid.get_x()))

    def rotate(self, amount):
        self.current_rotation += amount

        self.set_attribute("vertex_a", Vertex(Vector2D(self.centroid, self.vertex_a).rotate(amount).get_endpoint()))
        self.set_attribute("vertex_b", Vertex(Vector2D(self.centroid, self.vertex_b).rotate(amount).get_endpoint()))
        self.set_attribute("vertex_c", Vertex(Vector2D(self.centroid, self.vertex_c).rotate(amount).get_endpoint()))

        return self
