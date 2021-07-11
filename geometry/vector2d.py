import math

class Vector2D:
    def __init__(self, start_vertex, end_vertex, magnitude=None):
        self.locked = False
        self.end_vertex = end_vertex
        self.relation_point = start_vertex
        self.magnitude_limit = math.inf
        self.magnitude = magnitude
        self.delta_x = end_vertex.get_x() - start_vertex.get_x()
        self.delta_y = end_vertex.get_y() - start_vertex.get_y()

        self.alpha = math.acos(self.delta_y / self.get_magnitude())
        self.beta = (math.pi / 2) - self.alpha


    def normalize(self):
        return self.set_magnitude(1)

    def get_magnitude(self):
        self.set_attribute("magnitude", math.hypot(self.delta_x, self.delta_y))
        if self.magnitude == 0:
            raise AttributeError("Zero magnitude vector cannot exist")
        return self.magnitude

    def set_magnitude(self, new_mag):
        self.set_attribute("magnitude", new_mag if new_mag < self.magnitude_limit else self.magnitude_limit)
        unit = self.get_unit()
        self.set_attribute("delta_x", unit.delta_x * self.magnitude)
        self.set_attribute("delta_y", unit.delta_x * self.magnitude)
        return self

    def scale(self, scale):
        self.set_attribute("delta_x", self.delta_x * scale)
        self.set_attribute("delta_y", self.delta_y * scale)
        return self

    def set_relation_point(self, new_point):
        self.set_attribute("relation_point", new_point)
        return self

    def get_normal(self):
        copy = self
        return copy.rotate(-math.pi / 2)

    def get_unit(self):
        copy = self
        return copy.scale(1/self.magnitude)

    def translate(self, amount):
        self.relation_point.translate(amount)
        return self

    def get_linear_description(self):
        return {
            "a": self.delta_x / self.delta_y,
            "b": self.relation_point.y
        }

    def set_position(self, vertex):
        return self.set_relation_point(vertex)

    def rotate(self, angle):
        """
        Rotates vector by given angle

        :param angle: Angle in radians
        :return: self
        """
        dx = self.delta_x * math.cos(angle) - self.delta_y * math.sin(angle)
        dy = self.delta_x * math.sin(angle) + self.delta_y * math.cos(angle)

        reset_mag = math.hypot(dx, dy)/self.magnitude

        self.set_attribute("delta_x", dx/reset_mag)
        self.set_attribute("delta_y", dy/reset_mag)

        return self

    def get_endpoint(self):
        return self.relation_point.get_x() + self.delta_x, self.relation_point.get_y() + self.delta_y

    @staticmethod
    def Lock(vector):
        vector.locked = True
        return vector

    def set_attribute(self, key, value):
        if self.locked:
            raise AttributeError("Vector is locked. Cannot change any attributes")
        else:
            self.__setattr__(key, value)
