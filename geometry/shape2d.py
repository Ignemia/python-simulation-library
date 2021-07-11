from geometry.vector2d import Vector2D
from geometry.vertex import Vertex


class Shape2D:
    def __init__(self):
        self.relative_to = None
        self.position = [0, 0]
        self.movement = [0, 0]
        self.locked = False
        self.current_rotation = 0

    def get_x(self):
        if self.relative_to is not None:
            return self.relative_to.position[0] + self.position[0]
        return self.position[0]

    def get_y(self):
        if self.relative_to is not None:
            return self.relative_to.position[1] + self.position[1]
        return self.position[1]

    def get_movement_vector(self):
        return Vector2D(Vertex((0, 0)), Vertex(self.movement))

    def set_relative_object(self, o):
        return self.set_attribute("relative_to", o)

    def set_attribute(self, key, value):
        if self.locked:
            raise AttributeError("Vector is locked. Cannot change any attributes")
        else:
            self.set_attribute(key, value)
        return self

    def move(self, amount):
        return self.set_attribute("position", (self.position[0] + amount[1], self.position[1] + amount[1]))

    def move_x(self, amount):
        return self.move((self.position[0] + amount, 0))

    def move_y(self, amount):
        return self.move((0, self.position[1] + amount))

    @staticmethod
    def Lock(o):
        o.locked = True
        return o
