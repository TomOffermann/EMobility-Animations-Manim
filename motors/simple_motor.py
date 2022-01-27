from manim import *


def create_simple_motor() -> Mobject:
    c_inner = Circle(1.4, GREY_D).set_fill(GREY_B, 1).set_z_index(3)
    c_middle = Circle(1.6, GREY_D).set_fill(WHITE, 1).set_z_index(2)
    c_outer = Circle(2, GREY_D).set_fill(GREY_B, 1).set_z_index(1)

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

    return VGroup(c_inner, c_middle, c_outer, stand)


class SimpleMotor(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        rotor = Text("Rotor", color=BLACK).set_x(-5.5).set_y(2)
        rotor_line = VGroup(
            Line([-6.4, 1.65, 0], [-3.5, 1.65, 0], color=BLACK),
            Line([-3.5, 1.65, 0], [-0.5, 0.5, 0], color=BLACK).set_z_index(10),
        )

        stator = Text("Stator", color=BLACK).set_x(5.5).set_y(-1.1)
        stator_line = VGroup(
            Line([6.4, -1.45, 0], [3.7, -1.45, 0], color=BLACK),
            Line([3.7, -1.45, 0], [1.3 * 1.8, -1.3 * 1.8, 0], color=BLACK).set_z_index(10),
        )

        self.add(create_simple_motor(), rotor, rotor_line, stator, stator_line)
