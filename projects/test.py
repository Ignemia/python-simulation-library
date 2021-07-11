# from geometry.triangle import Triangle
from view.color import Color
from view.math.vertex import Vertex
from view.shapes.rectangle import Rectangle
from view.shapes.triangle import Triangle
from view.window import Window
import math

def rot(app):
    for o in app.draw_objects:
        o.rotate(math.pi / (10_000* app.last_frame_time or 1))

def setup(app):
    cv = app.get_canvas()

    vertices = [Vertex(cv, (0, 100)), Vertex(cv, (75, -50)), Vertex(cv, (-75, -50))]

    app.add_draw_object(Triangle(cv, vertices).set_color(Color(255, 200, 200)))
    app.add_draw_object(Rectangle(cv, Vertex(cv, (0, 0)), (40, 80)).set_color(Color(255, 0, 0)))
    app.add_update_function(("rotation", rot))


window = Window((1280, 720), background=Color(27, 27, 27))
window.setup = setup
window.run()
