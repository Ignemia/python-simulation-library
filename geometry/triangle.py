import math

from geometry.shape2d import Shape2D
from geometry.vector2d import Vector2D
from geometry.vertex import Vertex


class Triangle(Shape2D):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise TypeError(f"Triangle requires exactly 3 vertices {len(vertices)} given")
        super().__init__()

        self.vertices = vertices
        self.centroid = self.get_centroid()
        self.position = (self.centroid.get_x(), self.centroid.get_y())

        self.center_vectors = [Vector2D(self.centroid, v) for v in self.vertices]

        self.vector_ab = Vector2D(self.vertices[0], self.vertices[1])
        self.vector_bc = Vector2D(self.vertices[1], self.vertices[2])
        self.vector_ca = Vector2D(self.vertices[2], self.vertices[0])

        self.circumference = self.vector_ab.get_magnitude() + self.vector_bc.get_magnitude() + self.vector_ca.get_magnitude()
        heron_s = self.circumference / 2
        heron_a = (heron_s - self.vector_ab.get_magnitude())
        heron_b = (heron_s - self.vector_bc.get_magnitude())
        heron_c = (heron_s - self.vector_ca.get_magnitude())
        self.area = math.sqrt(heron_s * heron_a * heron_b * heron_c)

    def get_centroid(self):
        return Vertex((
            sum([x.get_x() for x in self.vertices]) / 3,
            sum([x.get_y() for x in self.vertices]) / 3
        ))

    def move(self, amount):
        self.centroid.translate(amount)
        return self.set_attribute("position", (self.centroid.get_x(), self.centroid.get_x()))

    def rotate(self, amount):
        # print(amount)
        self.current_rotation += amount
        self.current_rotation %= 2 * math.pi
        # pprint(self.current_rotation)

        for i, v in enumerate(self.center_vectors):
            self.vertices[i].set_position(v.rotate(amount).get_endpoint())

        return self
