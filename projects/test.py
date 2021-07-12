# from geometry.triangle import Triangle

import numpy.random as random

from view.color import Color
from view.math.vertex import Vertex
from view.shapes.circle import Circle
from view.window import Window


def object_update(app):
    for o in app.draw_objects:
        o.update(app.last_frame_time or 0.001)
        # '''sometimes is do be 0.000 so the or statement to negate that'''
        # o.rotate(math.pi / (10_000_000 * (app.last_frame_time or 0.001)))


def setup(app):
    app.add_update_function(("o_update", object_update))
    cv = app.get_canvas()
    half_w = int(cv["width"]) / 2
    half_h = int(cv["height"]) / 2
    for i in range(100):
        center = Vertex(cv, (random.randint(-half_w, half_w), random.randint(-half_h, half_h)))
        c = Circle(cv, center, random.randint(5, 25)).set_color(Color.Get_Random()).set_movement_vector((20, 20))
        app.add_draw_object(c)
    # c2 = Circle(cv, Vertex(cv, (50,50)), 10).set_color(Color.Get_Random()).set_movement_vector((20,20))
    # app.add_draw_object(c)
    # app.add_draw_object(c2)


window = Window((1280, 720), background=Color(27, 27, 27))
window.setup = setup
window.run()
