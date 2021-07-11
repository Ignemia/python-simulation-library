from geometry.ellipse import Ellipse as GEllipse
from view.components.drawObject import DrawObject


class Ellipse(DrawObject, GEllipse):
    def __init__(self, canvas, position, radii):
        super(Ellipse, self).__init__(canvas)
        self.set_position(position)
        self.radii = radii

    def draw(self):
        self.canvas.create_oval(self.get_x() - self.radii[0], self.get_y() - self.radii[1],
                                self.get_x() + self.radii[0], self.get_y() + self.radii[1],
                                fill=self.color["fill"].hex)
