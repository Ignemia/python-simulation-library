from view.color import Color
from view.components.drawObject import DrawObject
from geometry.vertex import Vertex as GVertex

class Vertex(DrawObject, GVertex) :
    """
        Vertex Object
        Inherits from DrawObject and geometry.Vertex
    """

    def __init__(self, canvas,  position, color=Color.Get_Random()):
        GVertex.__init__(self, position)
        DrawObject.__init__(self, canvas)
        self.set_position(position)
        self.z = 0
        self.radius = 3
        self.set_color(color)
        self.original.set_immutable()

    def draw(self):
        self.canvas.create_oval(self.get_x()-self.radius, self.get_y()-self.radius, self.get_x()+self.radius, self.get_y()+self.radius, fill=self.color["fill"].hex, outline="")
        return self

    def set_attribute(self, key, value):
        if self.locked:
            raise AttributeError("Vector is locked. Cannot change any attributes")
        else:
            self.__setattr__(key, value)
        return self
