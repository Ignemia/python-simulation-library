from geometry.vector2d import Vector2D as GVector
from view.color import Color
from view.components.drawObject import DrawObject


class Vector(DrawObject, GVector):
    def __init__(self, canvas, vertex1, vertex2):
        super().__init__(canvas)
        super().__init__(vertex1, vertex2)

        self.vertex1 = vertex1.set_color(Color(100,255,100))
        self.vertex2 = vertex2.set_color(Color(255,100,100))

    def draw(self):
        pt1 = self.vertex1.get_draw_position()
        pt2 = self.vertex2.get_draw_position()
        self.canvas.create_line(pt1[0], pt1[1], pt2[0], pt2[1])
        self.vertex1.draw()
        self.vertex2.draw()
        self.canvas.pack()
