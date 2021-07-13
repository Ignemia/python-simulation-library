class FieldSpot:
    def __init__(self, value, index, position, neighbors, field):
        self.position = position
        self.index = index
        self.value = value
        self.neighbors = neighbors
        self.field = field
        self.static = False

    def make_Static(self):
        self.static = True
        return self

    def get_neighbors_values(self):
        return {
            "nw": self.field.spots[self.neighbors[0]],
            "n": self.field.spots[self.neighbors[1]],
            "ne": self.field.spots[self.neighbors[2]],
            "w": self.field.spots[self.neighbors[3]],
            "e": self.field.spots[self.neighbors[4]],
            "sw": self.field.spots[self.neighbors[5]],
            "s": self.field.spots[self.neighbors[6]],
            "se": self.field.spots[self.neighbors[7]]
        }

    def set_value(self, value):
        if self.static:
            raise Exception("Field is static cannot be modified")
        self.value = value
        return self
