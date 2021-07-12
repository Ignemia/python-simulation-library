from view.color import Color
from view.math.vertex import Vertex


class DrawObject(object):
    def __init__(self, canvas, *args):
        self.canvas = canvas
        self.destroy = False
        self.locked = False
        self.centroid = None
        self.color = {
            "fill": Color.Get_Random(),
            "stroke": Color.Get_Random()
        }
        self.stroke_strength = 0

    def set_color(self, color):
        self.color["fill"] = color
        return self

    def set_stroke(self, color, strength):
        self.color["stroke"] = color
        self.stroke_strength = strength
        return self

    def is_dead(self):
        return self.locked

    def set_position(self, new_position):
        if self.centroid is None:
            self.centroid = Vertex(self.canvas, new_position)
        else:
            self.centroid.set_position(new_position)

        return self.set_attribute("position", (self.centroid.get_x(), self.centroid.get_y()))

    def set_destructible(self):
        self.set_attribute("destroy", True)
        return self

    def remove(self):
        self.set_attribute("locked", True)
        return self

    def set_attribute(self, key, value):
        self.__setattr__(key, value)
        return self

    @staticmethod
    def Normalize(canvas, position):
        return position[0] - int(canvas["width"]) / 2, position[1] - int(canvas["height"]) / 2

    @staticmethod
    def Denormalize(canvas, position):
        return position[0] + int(canvas["width"]) / 2, position[1] + int(canvas["height"]) / 2
