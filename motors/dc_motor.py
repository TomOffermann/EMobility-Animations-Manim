from manim import *


def create_dc_motor() -> Mobject:
    r_inner = Rectangle(GREY_D, 2.8, 0.3).set_fill([RED, BLUE], 1).set_z_index(5).rotate(1)
    c_inner = Circle(0.68, GREY_B).set_fill(GREY_B, 1).set_z_index(4)
    c_hidden = Circle(0.75, WHITE).set_fill(WHITE, 1).set_z_index(3)
    c_middle = Circle(1.6, GREY_D).set_fill(WHITE, 1).set_z_index(2)
    c_outer = Circle(2, GREY_D).set_fill([RED, BLUE], 1).set_z_index(1).rotate(1 / 4 * np.pi)
    a = Arc(0.7, 1.2, np.pi - 0.4, color=GOLD_D, stroke_width=10).set_z_index(4)
    b = Arc(0.7, 0.8, -np.pi + 0.4, color=GOLD_D, stroke_width=10).set_z_index(4)
    upper_rect = (
        Rectangle(GREY_D, height=1, width=0.3).set_fill([GREY_C, BLUE], 1).set_z_index(2).set_y(1.09).rotate(np.pi)
    )
    lower_rect = Rectangle(GREY_D, height=1, width=0.3).set_fill([GREY_C, RED], 1).set_z_index(2).set_y(-1.09)
    stand = (
        Polygon(
            [-2, -2.2, 0],
            [2, -2.2, 0],
            [2, -2, 0],
            [1.75, -2, 0],
            [np.sqrt(2), -np.sqrt(2), 0],
            [-np.sqrt(2), -np.sqrt(2), 0],
            [-1.75, -2, 0],
            [-2, -2, 0],
            color=GREY_D,
        )
        .set_fill(GRAY_C, 1)
        .set_z_index(0)
    )

    return VGroup(c_inner, c_middle, c_outer, stand, r_inner, a, b, upper_rect, lower_rect, c_hidden)


class DCMotor(Scene):
    def construct(self):

        rotor = Text("Rotor", color=BLACK).set_x(-5.5).set_y(2)
        rotor_line = VGroup(
            DashedVMobject(Line([-6.4, 1.65, 0], [-3.5, 1.65, 0], color=BLACK), num_dashes=12),
            DashedVMobject(Line([-3.5, 1.65, 0], [-0.5, -0.5, 0], color=BLACK).set_z_index(10)),
            DashedVMobject(Line([-1.96, 0.545, 0], [-0.5, 0.545, 0], color=BLACK).set_z_index(10), num_dashes=7),
        )
        stator = Text("Stator", color=BLACK).set_x(5.5).set_y(-1.1)
        stator_line = VGroup(
            DashedVMobject(Line([6.4, -1.45, 0], [3.7, -1.45, 0], color=BLACK), num_dashes=10),
            DashedVMobject(Line([3.7, -1.45, 0], [1.3 * 1.8, -1.3 * 1.8, 0], color=BLACK).set_z_index(10), num_dashes=7),
        )

        brushes = Text("Bürsten", color=BLACK).set_x(5).set_y(3)
        brushes_line = VGroup(
            DashedVMobject(Line([6.4, 2.65, 0], [3.7, 2.65, 0], color=BLACK), num_dashes=10),
            DashedVMobject(Line([3.15, 1.09 * 1.8, 0], [0, 1.09 * 1.8, 0], color=BLACK).set_z_index(3), num_dashes=11),
            DashedVMobject(Line([3.7, 2.65, 0], [0, -1.09 * 1.8, 0], color=BLACK).set_z_index(3), num_dashes=22),
        )

        self.camera.background_color = WHITE
        everything = create_dc_motor()
        self.add(everything.scale(1.8), rotor, rotor_line, stator, stator_line, brushes, brushes_line)
