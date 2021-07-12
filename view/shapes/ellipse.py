from geometry.ellipse import Ellipse as GEllipse
from view.components.drawObject import DrawObject


class Ellipse(DrawObject, GEllipse):
    def __init__(self, canvas, position, radii):
        DrawObject.__init__(self, canvas)
        GEllipse.__init__(self, position, radii)
        self.set_position(position)

    def draw(self):
        pos = self.get_draw_position(self.get_position())

        self.canvas.create_oval(pos[0] - self.radii[0], pos[1] - self.radii[1],
                                pos[0] + self.radii[0], pos[1] + self.radii[1],
                                fill=self.color["fill"].hex)
