from geometry.triangle import Triangle as GTriangle
from view.components.drawObject import DrawObject


class Triangle(DrawObject, GTriangle):
    def __init__(self, canvas, vertices):
        DrawObject.__init__(self, canvas)
        GTriangle.__init__(self, vertices)

    def draw(self):
        vert_map = []
        p = self.get_position(self.get_canvas_center_position())
        for v in self.vertices:
            vert_map.extend([v.get_x(p), v.get_y(p)])
        self.canvas.create_polygon(vert_map, fill=self.color["fill"].hex)
        return self
