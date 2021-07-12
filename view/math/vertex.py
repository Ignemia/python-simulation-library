from geometry.vertex import Vertex as GVertex
from view.color import Color

VERTEX_RADIUS = 3


class Vertex(GVertex):

    def __init__(self, canvas, position):
        GVertex.__init__(self, position)
        self.canvas = canvas
        self.dead = False
        self.centroid = None
        self.color = {
            "fill": Color.Get_Random(),
            "stroke": Color.Get_Random()
        }

    def is_dead(self):
        return self.dead

    def kill(self):
        self.dead = True

    def get_draw_position(self):
        return self.get_x() + int(self.canvas["width"]) / 2, self.get_y() + int(self.canvas["height"]) / 2

    def draw(self):
        draw_position = self.get_draw_position()
        self.canvas.create_oval(draw_position[0] - VERTEX_RADIUS, draw_position[1] - VERTEX_RADIUS, draw_position[0] + VERTEX_RADIUS,
                                draw_position[1] + VERTEX_RADIUS, fill=self.color["fill"].hex, outline="")
        return self
