# from geometry.triangle import Triangle
import math

import numpy.random as random

from view.color import Color
from view.math.vertex import Vertex
from view.shapes.triangle import Triangle
from view.window import Window


def object_update(app):
    for o in app.draw_objects:
        d_t = app.get_delta_t()
        o.update(d_t)
        o.apply_acceleration((0, -9.8), d_t)
        o.rotate(math.pi * 2 * d_t)


def setup(app):
    app.add_update_function(("o_update", object_update))
    cv = app.get_canvas()
    half_w = int(cv["width"]) / 2
    half_h = int(cv["height"]) / 2
    for i in range(100):
        # center = Vertex(cv, (random.randint(-half_w, half_w), random.randint(-half_h, half_h)))
        vel_y = random.randint(0, 100) - 50
        vel_x = random.randint(0, 100) - 50
        # c = Square(cv, center, random.randint(5, 25)).set_color(Color.Get_Random()).set_movement_vector((vel_y, vel_x))

        v1 = Vertex(cv, (random.randint(0, 200) - 100, random.randint(0, 200) - 100))
        v2 = Vertex(cv, (random.randint(0, 200) - 100, random.randint(0, 200) - 100))
        v3 = Vertex(cv, (random.randint(0, 200) - 100, random.randint(0, 200) - 100))

        c = Triangle(cv, [v1, v2, v3]).set_color(Color.Get_Random()).set_movement_vector((vel_y, vel_x))
        app.add_draw_object(c)
    # c2 = Circle(cv, Vertex(cv, (50,50)), 10).set_color(Color.Get_Random()).set_movement_vector((20,20))
    # app.add_draw_object(c)
    # app.add_draw_object(c2)


window = Window((1280, 720), background=Color(27, 27, 27))
window.setup = setup
window.run()
