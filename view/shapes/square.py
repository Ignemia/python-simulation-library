from view.shapes.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, canvas, position, side):
        Rectangle.__init__(self, canvas, position, (side, side))
