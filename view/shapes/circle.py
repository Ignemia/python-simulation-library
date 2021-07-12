from view.shapes.ellipse import Ellipse


class Circle(Ellipse):
    def __init__(self, canvas, position, radius):
        Ellipse.__init__(self, canvas, position, (radius, radius))
