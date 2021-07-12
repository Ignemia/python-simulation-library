from geometry.triangle import Triangle as GTriangle
from view.components.drawObject import DrawObject


class Triangle(DrawObject, GTriangle):
    def __init__(self, canvas, vertices):
        DrawObject.__init__(self, canvas)
        GTriangle.__init__(self, vertices)

    def draw(self):
        (ax, ay) = self.get_draw_position(self.vertices[0].get_position(self.get_position()))
        (bx, by) = self.get_draw_position(self.vertices[1].get_position(self.get_position()))
        (cx, cy) = self.get_draw_position(self.vertices[2].get_position(self.get_position()))

        positions = ax, ay, bx, by, cx, cy
        self.canvas.create_polygon(positions, fill=self.color["fill"].hex)
        return self
