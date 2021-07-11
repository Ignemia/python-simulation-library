from view.shapes.ellipse import Ellipse


class Circle(Ellipse):
    def __init__(self, canvas, position, radius):
        super().__init__(canvas, position, (radius, radius))