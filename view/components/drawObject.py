from view.color import Color


class DrawObject(object):
    def __init__(self, canvas, *args):
        self.args = args
        self.canvas = canvas
        self.position = None
        self.destroy = False
        self.locked = False
        self.immutable = False
        self.original = self
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

    def get_normal_x(self):
        return self.position[0] - int(self.canvas["width"]) / 2

    def get_normal_y(self):
        return self.position[1] - int(self.canvas["height"]) / 2

    def get_x(self):
        return self.position[0]

    def get_y(self):
        return self.position[1]

    def set_position(self, new_position):
        c_w = int(self.canvas["width"]) / 2
        c_h = int(self.canvas["height"]) / 2

        return self.set_attribute("position", (int(new_position[0]) + c_w, (-int(new_position[1]) + c_h)))

    def set_destructible(self):
        self.set_attribute("destroy", True)
        return self

    def remove(self):
        self.set_attribute("locked", True)
        return self

    def set_immutable(self):
        self.immutable = True
        return self

    def set_attribute(self, key, value):
        if self.immutable:
            raise AttributeError("Object is immutable")
        else:
            self.__setattr__(key, value)

        return self

    @staticmethod
    def Normalize(canvas, position):
        return position[0] - int(canvas["width"]) / 2, position[1] - int(canvas["height"]) / 2

    @staticmethod
    def Denormalize(canvas, position):
        return position[0] + int(canvas["width"]) / 2, position[1] + int(canvas["height"]) / 2
