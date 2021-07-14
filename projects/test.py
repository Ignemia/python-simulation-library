import math

from numpy import random

from view.color import Color
from view.math.vertex import Vertex
from view.shapes.triangle import Triangle
from view.window import Window

WIDTH = 400
HEIGHT = WIDTH
SCALE = 2
SIZE = 40


def checkboard_draw_function(field, app):
    for spot in field.spots:
        app.canvas.create_rectangle(spot.position[0] * SIZE * SCALE, spot.position[1] * SIZE * SCALE,
                                    spot.position[0] * SIZE * SCALE + SIZE * SCALE, spot.position[1] * SCALE * SIZE + SIZE * SCALE,
                                    fill="#000" if spot.value == 1 else None)


def object_update(app):
    # for f in app.fields.values():

    for o in app.draw_objects:
        d_t = app.get_delta_t()
        o.update(d_t)
        o.apply_acceleration((0, -9.8), d_t)
        o.rotate(math.pi * 2 * d_t)


def update_function(field, _app):
    pass


def default_value_assignment(spot):
    spot.value = 1 if ((spot.position[0] + spot.position[1]) % 2 == 1) else 0

def setup(app):
    app.create_field("checkerboard", update_function, default_value_assignment, (WIDTH, HEIGHT), 1 / SIZE)
    app.add_update_function(("o_update", object_update))
    app.add_field_draw_function("checkerboard", checkboard_draw_function)
    cv = app.get_canvas()
    half_w = int(cv["width"]) / 2
    half_h = int(cv["height"]) / 2
    for i in range(50):
        # center = Vertex(cv, (random.randint(-half_w, half_w), random.randint(-half_h, half_h)))
        vel_y = random.randint(0, 100) - 50
        vel_x = random.randint(0, 100) - 50
        # c = Square(cv, center, random.randint(5, 25)).set_color(Color.Get_Random()).set_movement_vector((vel_y, vel_x))

        v1 = Vertex(cv, (random.randint(0, 50) - 25, random.randint(0, 50) - 25))
        v2 = Vertex(cv, (random.randint(0, 50) - 25, random.randint(0, 50) - 25))
        v3 = Vertex(cv, (random.randint(0, 50) - 25, random.randint(0, 50) - 25))

        c = Triangle(cv, [v1, v2, v3]).set_color(Color.Get_Random()).set_movement_vector((vel_y, vel_x))
        app.add_draw_object(c)
    # c2 = Circle(cv, Vertex(cv, (50,50)), 10).set_color(Color.Get_Random()).set_movement_vector((20,20))
    # app.add_draw_object(c)
    # app.add_draw_object(c2)


window = Window((WIDTH * SCALE, HEIGHT * SCALE), background=Color(255, 255, 255))
window.setup = setup
window.run()
