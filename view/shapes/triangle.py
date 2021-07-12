from geometry.triangle import Triangle as GTriangle
from view.components.drawObject import DrawObject


class Triangle(DrawObject, GTriangle):
    def __init__(self, canvas, vertices):
        DrawObject.__init__(self, canvas)
        GTriangle.__init__(self, vertices)

    def draw(self):
        (ax, ay) = DrawObject.Denormalize(self.canvas, self.vertices[0].get_position())
        (bx, by) = DrawObject.Denormalize(self.canvas, self.vertices[1].get_position())
        (cx, cy) = DrawObject.Denormalize(self.canvas, self.vertices[2].get_position())

        positions = ax, ay, bx, by, cx, cy
        self.canvas.create_polygon(positions, fill=self.color["fill"].hex)
        return self
