import time
import tkinter as Tk

from field.field import Field
from view.color import parse_hex


class Window(Tk.Tk):
    def __init__(self, size, background=parse_hex("#ffffff"), title="Main window"):
        Tk.Tk.__init__(self)
        self.current_background = background
        self.geometry(f"{size[0]}x{size[1]}")
        self.config(background=self.current_background.hex)
        self.title(title)
        self.resizable(0, 0)

        self.canvas = Tk.Canvas(self, width=size[0], height=size[1], bg=self.current_background.hex)
        self.canvas.pack()

        self.draw_objects = []

        self.app_time = 0
        self.app_init_time = time.time()
        self.last_frame_time = 0

        self.update_functions = []
        self.field_draw_functions = []
        self.setup = None
        self.physics = None

        self.fields = {}

    def get_delta_t(self, units="s"):
        ft = self.last_frame_time or 0.001
        if units == "ms":
            return ft * 1000
        elif units == "us":
            return ft * 1000_000
        elif units == "ns":
            return ft * 1_000_000_000
        elif units == "min":
            return ft / 60
        elif units == "h":
            return ft / 3600
        else:
            return ft

    def redraw(self):
        # pass
        self.canvas.update()
        self.canvas.delete(Tk.ALL)

        for f in self.field_draw_functions:
            f[1](self.fields[f[0]], self)

        for o in self.draw_objects:
            if o.is_dead():
                continue
            o.draw()
        return self

    def get_canvas(self):
        return self.canvas

    def filter_objects(self):
        return self

    def add_draw_object(self, item):
        self.draw_objects.append(item)
        return self

    def optimize(self):
        self.draw_objects.remove(lambda x: x.locked and x.destroy)
        return self

    def update_scene(self):
        m_time_start = time.time() - self.app_init_time

        if self.physics is not None:
            self.physics()

        for f in self.update_functions:
            f[1](self)

        self.filter_objects()
        # self.optimize()

        self.redraw()
        self.update()

        self.app_time = time.time() - self.app_init_time
        self.last_frame_time = self.app_time - m_time_start

        return self.last_frame_time

    def add_update_function(self, func):
        self.update_functions.append(func)
        return self

    def add_field_draw_function(self, fname, func):
        self.field_draw_functions.append((fname, func))
        return self

    def remove_update_function(self, func_id):
        self.update_functions.remove(lambda x: x[0] == func_id)
        return self

    def add_physics_function(self, func):
        self.physics = func
        return self

    def set_background(self, color):
        self.current_background = color
        self.config(background=self.current_background.hex)
        self.canvas.config(background=self.current_background.hex)
        return self

    def run(self):
        if self.setup is None:
            raise Exception("Setup function not defined. Please create at least an empty function.")
        self.setup(self)
        while True:
            self.update_scene()

    def create_field(self, name, recalc_function, assign_start_value_function, window_size, density=1, default_value=0, past_edge_extension=0):
        self.fields[name] = Field(name, recalc_function, assign_start_value_function, window_size, self, density, default_value, past_edge_extension)
