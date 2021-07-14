import math

from field.fieldSpot import FieldSpot


class Field:
    def __init__(self, name, recalc_function, assign_start_value_function, window_size, app=None, density=1, default_value=0, past_edge_extension=0):
        if past_edge_extension != 0:
            raise Exception("Currently not supporting past_edge_extension")
        self.name = name
        self.recalc_function = recalc_function
        self.density = density
        self.past_edge_extension = past_edge_extension
        self.spots = []
        self.initialize(window_size, default_value)
        self.width = window_size[0]
        self.app = app
        self.assign_values(assign_start_value_function)

    def get_value_at(self, x, y):
        sum_values = 0
        count = 0

        index_0 = self.density * (self.width * y * self.density + x)
        next_row = self.density * (self.width - 1)

        for y_shift in range(self.density):
            for x_shift in range(self.density):
                sum_values += self.spots[index_0 + x_shift + y_shift * next_row]
                count += 1

        return sum_values / count

    def update(self):
        return self.recalc_function(self, self.app)

    def initialize(self, window_size, default_value):
        w = (window_size[0] + self.past_edge_extension) * self.density
        self.width = w
        h = (window_size[1] + self.past_edge_extension) * self.density
        spot_count = w * h
        print(spot_count)
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

            self.spots.append(FieldSpot(default_value, i, pos, neighbors, self))

    def assign_values(self, assignment_function):
        for spot in self.spots:
            assignment_function(spot)

    def print(self):
        line = ""
        print("printing")
        for spot in self.spots:
            if spot.index % (self.width * self.density) != 0:
                line += str(spot.value)
            else:
                print(line)
                line = ""
