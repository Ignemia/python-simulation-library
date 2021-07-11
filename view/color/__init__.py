import random

def get_limited(value, top=1, bottom=0):
    if value > top:
        return top
    if value < bottom:
        return bottom
    return value


def get_hex(r, g, b):
    temp_r = hex(get_limited(r, 255, 0))
    temp_g = hex(get_limited(g, 255, 0))
    temp_b = hex(get_limited(b, 255, 0))

    s_red = temp_r[2:]
    s_green = temp_g[2:]
    s_blue = temp_b[2:]

    return f"#{('0' * (2 - len(s_red))) + s_red}{('0' * (2 - len(s_green))) + s_green}{('0' * (2 - len(s_blue))) + s_blue}"


def parse_hex(string):
    c = string[1:]
    out_color_list = []
    for i in range(0, 6, 2):
        out_color_list.append(c[i:i + 2])
    return Color(int(out_color_list[0], 16), int(out_color_list[1], 16), int(out_color_list[2], 16))


class Color:
    def __init__(self, r=0, g=0, b=0, a=1):
        self.rgb = [int(round(r)), int(round(g)), int(round(b))]
        self.alpha = a
        self.hex = get_hex(self.rgb[0], self.rgb[1], self.rgb[2])

    def set_alpha(self, alpha):
        self.alpha = alpha
        return self

    def set_r(self, val):
        self.rgb[0] = get_limited(val, 255, 0)
        self.hex = get_hex(self.rgb[0], self.rgb[1], self.rgb[2])
        return self

    def set_g(self, val):
        self.rgb[1] = get_limited(val, 255, 0)
        self.hex = get_hex(self.rgb[0], self.rgb[1], self.rgb[2])
        return self

    def set_b(self, val):
        self.rgb[2] = get_limited(val, 255, 0)
        self.hex = get_hex(self.rgb[0], self.rgb[1], self.rgb[2])
        return self

    def get_mixed(self, second_color):
        r = get_limited(second_color.rgb[0] * (1 - self.alpha) + self.alpha * self.rgb[0], 255, 0)
        g = get_limited(second_color.rgb[1] * (1 - self.alpha) + self.alpha * self.rgb[1], 255, 0)
        b = get_limited(second_color.rgb[2] * (1 - self.alpha) + self.alpha * self.rgb[2], 255, 0)

        return Color(r, g, b)

    @staticmethod
    def Get_Random():
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
