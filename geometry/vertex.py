class Vertex:
    def __init__(self, position):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.locked = False
        self.relative_to = None

    def get_position(self):
        return self.get_x(), self.get_y()

    def get_x(self, relation_point=None):
        if relation_point is not None:
            return self.x + relation_point[0]

        if self.relative_to is not None:
            return self.x + self.relative_to.position[0]
        return self.x

    def get_y(self, relation_point=None):
        if relation_point is not None:
            return self.y + relation_point[1]

        if self.relative_to is not None:
            return self.y + self.relative_to.position[1]
        return self.y

    def set_position(self, new_position):
        self.set_attribute("position", new_position)
        self.set_attribute("x", new_position[0])
        self.set_attribute("y", new_position[1])

    def translate(self, amount):
        self.set_attribute("x", self.x + amount[0])
        self.set_attribute("y", self.y + amount[1])
        self.set_attribute("position", (self.x, self.y))
        return self

    def translate_x(self, amount):
        self.translate((amount, 0))
        return self

    def translate_y(self, amount):
        self.translate((0, amount))
        return self

    def set_attribute(self, key, value):
        if self.locked:
            raise KeyError("Vertex is locked")
        else:
            self.__setattr__(key, value)