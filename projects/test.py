# from geometry.triangle import Triangle
import math

from view.color import Color
from view.math.vertex import Vertex
from view.shapes.circle import Circle
from view.window import Window


def rot(app):
    for o in app.draw_objects:
        '''sometimes is do be 0.000 so the or statement to negate that'''
        o.rotate(math.pi / (10_000_000 * (app.last_frame_time or 0.001)))

def setup(app):
    cv = app.get_canvas()

    vertices = [Vertex(cv, (0, 100)), Vertex(cv, (75, -50)), Vertex(cv, (-75, -50))]

    # app.draw_objects.extend(vertices)
    # app.add_draw_object(Triangle(cv, vertices).set_color(Color(255, 200, 200)))
    # app.add_draw_object(Square(cv, Vertex(cv, (0, 0)), 80).set_color(Color(255, 0, 0)))
    app.add_draw_object(Circle(cv, Vertex(cv, (0, 0)), 80).set_color(Color(255, 0, 0)))
    app.add_update_function(("rotation", rot))


window = Window((1280, 720), background=Color(27, 27, 27))
window.setup = setup
window.run()
