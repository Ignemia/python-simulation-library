import math

from field.fieldSpot import FieldSpot


class Field:
    def __init__(self, name, recalc_function, window_size, density=1, default_value=0, past_edge_extension=1, app=None):
        self.name = name
        self.recalc_function = recalc_function
        self.density = density
        self.past_edge_extension = past_edge_extension
        self.initialize(window_size, default_value)
        self.spots = []
        self.width = window_size[0]
        self.app = app

    def get_value_at(self, x, y):
        sum_values = 0
        count = 0
        delta_y = int((self.density - 1) * self.width)
        for c_y in range(delta_y):
            y_ = (y * self.width * self.density) + c_y * self.width
            for c_x in range(self.density):
                c_x + x + y_
        return sum_values / count

    def update(self):
        return self.recalc_function(self.app)

    def initialize(self, window_size, default_value):
        w = window_size[0] + self.past_edge_extension * self.density
        self.width = w
        h = window_size[1] + self.past_edge_extension * self.density
        spot_count = w * h
        for i in range(int(spot_count)):
            pos = (i % w, math.floor(i / w))
            neighbors = []
            not_left = pos[0] % w != 0
            not_top = math.floor(pos[0] / w) != 0
            not_bottom = pos[0] % w != w - 1
            not_right = math.floor(pos[0] / w) != h - 1
            if not_top and not_left:  # 0
                neighbors.append(i - 1 - w)
            if not_top:  # 1
                neighbors.append(i - w)
            if not_top and not_right:  # 2
                neighbors.append(i + 1 - w)
            if not_left:  # 3
                neighbors.append(i - 1)
            if not_right:  # 4
                neighbors.append(i + 1)
            if not_bottom and not_left:  # 5
                neighbors.append(i - 1 + w)
            if not_bottom:  # 6
                neighbors.append(i + w)
            if not_right and not_right:  # 7
                neighbors.append(i + 1 + w)

            self.spots.append(FieldSpot(pos, default_value, neighbors, self))
