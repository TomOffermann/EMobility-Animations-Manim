from manim import *
from simple_motor import create_simple_motor
from math import pi


def circle_with_text(r: int, txt: str, color=BLACK, font_color=BLACK, fill_color=BLACK) -> Mobject:
    c = Circle(r, color).set_opacity(1).set_fill(fill_color)
    t = Circle()
    if txt == "X":
        t = Cross(c, stroke_color=font_color, scale_factor=0.6, stroke_width=4)
        return VGroup(c, t)
    elif txt == "O":
        t = Circle(r - 0.075, color=font_color)
        return VGroup(c, t)
    return Circle()


def create_points() -> Mobject:
    b_1 = circle_with_text(0.15, "X", BLUE, 22, BLACK, 1, BLUE)
    b_2 = circle_with_text(0.15, "O", BLUE, 22, BLACK, 1, BLUE)

    r_1 = circle_with_text(0.15, "X", RED, 22, BLACK, 1, RED)
    r_2 = circle_with_text(0.15, "O", RED, 22, BLACK, 1, RED)

    g_1 = circle_with_text(0.15, "X", GREEN, 22, BLACK, 1, GREEN)
    g_2 = circle_with_text(0.15, "O", GREEN, 22, BLACK, 1, GREEN)

    s = 1.8

    b_1.set_x(0).set_y(s)
    b_2.set_x(0).set_y(-s)

    r_1.set_x(np.sin(2 / 3 * pi) * s).set_y(np.cos(2 / 3 * pi) * s)
    r_2.set_x(np.sin(2 / 3 * pi - pi) * s).set_y(np.cos(2 / 3 * pi - pi) * s)

    g_1.set_x(np.sin(4 / 3 * pi) * s).set_y(np.cos(4 / 3 * pi) * s)
    g_2.set_x(np.sin(4 / 3 * pi - pi) * s).set_y(np.cos(4 / 3 * pi - pi) * s)

    return VGroup(b_1, b_2, r_1, r_2, g_1, g_2).set_z_index(10)


class ACMotor(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        everything = VGroup(create_simple_motor(), create_points())
        self.add(everything.scale(1.8))


class ExampleSineWaves(Scene):
    def get_sine_wave(self, deg: int, color) -> Mobject:
        return FunctionGraph(
            lambda x: 2 * np.sin(0.75 * (x) + deg * 2 / 3 * pi), x_range=[-6, 6, 1 / 0.75], color=color
        )

    def get_line(self, deg, start) -> Mobject:
        y = 2 * np.sin(start * 0.75 + deg * 2 / 3 * pi)
        return DashedVMobject(
            Line(start=[start, y + 0.5, 0], end=[start + (2 / 3 * pi) / 0.75, y + 0.5, 0], color=BLACK)
        )

    def construct(self):
        grid = Axes(
            x_length=11,
            y_length=5.5,
            x_range=[-5.5 * 0.75, 5.5 * 0.75, 2],
            y_range=[-2.0, 2.0, 1],
            tips=False,
            axis_config={
                "color": BLACK,
                "stroke_width": 2,
                "include_numbers": True,
                "decimal_number_config": {"num_decimal_places": 0, "include_sign": False, "color": BLACK},
            },
        )

        f_1 = self.get_sine_wave(0, BLUE)
        f_2 = self.get_sine_wave(1, RED)
        f_3 = self.get_sine_wave(2, GREEN)

        l_1 = self.get_line(0, pi / 2 - 1)
        l_2 = self.get_line(1, -pi + 2 / 3 * pi - 2 / 3)
        l_3 = self.get_line(2, -pi - 1 / 3)

        tags = VGroup(
            MathTex(r"^*", color=BLACK).set_x(-2.45).set_y(2.7),
            MathTex(r"^*", color=BLACK).set_x(-0.9).set_y(2.2),
            MathTex(r"^*", color=BLACK).set_x(1.4).set_y(1.6),
        )

        self.camera.background_color = WHITE
        everything = VGroup(grid, f_1, f_2, f_3)
        txt = MathTex(r"^*\hspace{1mm}(\frac{2\pi}{3} rad = 120^{\circ})", color=BLACK)
        self.add(
            Rectangle(WHITE, height=1.5, width=4.1)
            .set_opacity(0)
            .set_fill(WHITE, 0.6)
            .set_x(-3)
            .set_y(-1.15)
            .set_z_index(100)
        )
        self.add(everything.set_y(0.5), txt.set_x(-3).set_y(-1.15).set_z_index(200), l_1, l_2, l_3, tags)
