from view.components.drawObject import DrawObject
from geometry.triangle import Triangle as GTriangle

class Triangle(DrawObject, GTriangle):
    def __init__(self, canvas, vertices):
        DrawObject.__init__(self, canvas)
        GTriangle.__init__(self, vertices)

    def draw(self):
        positions = self.vertex_a.get_x(), self.vertex_a.get_y(), self.vertex_b.get_x(), self.vertex_b.get_y(), self.vertex_c.get_x(), self.vertex_c.get_y()
        self.canvas.create_polygon(positions, fill=self.color["fill"].hex)
        return self
