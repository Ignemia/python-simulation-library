from view.shapes.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, canvas, position, side):
        super().__init__(canvas, position, (side, side))
