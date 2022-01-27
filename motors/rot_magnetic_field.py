from manim import *
from math import pi


class SineWave(Scene):
    def get_sine_wave(self, dx=0, amplitude=1, frequenzy=1, color=BLUE) -> Mobject:
        return FunctionGraph(
            lambda x: amplitude * np.sin(frequenzy * (x) + dx), x_range=[0, 6, 1 / frequenzy], color=color
        )

    def get_c_1(self, t=0, f=1) -> Mobject:
        return Circle(np.sin(t * f) / pi, BLUE).set_x(-4).set_y(2).set_fill(BLUE, 1)

    def get_c_2(self, t=0, f=1) -> Mobject:
        return (
            Circle(np.sin(t * f + 2 / 3 * pi) / pi, RED)
            .set_x(2 * np.sin(2 / 3 * pi) - 4)
            .set_y(2 * np.cos(2 / 3 * pi))
            .set_fill(RED, 1)
        )

    def get_c_3(self, t=0, f=1) -> Mobject:
        return (
            Circle(np.sin(t * f + 4 / 3 * pi) / pi, GREEN)
            .set_x(2 * np.sin(4 / 3 * pi) - 4)
            .set_y(2 * np.cos(4 / 3 * pi))
            .set_fill(GREEN, 1)
        )

    def get_l_1(self, t=0) -> Mobject:
        return Line([-4, 0, 0], [-4, np.sin(t) * 3 * pi / 7, 0], color=BLUE)

    def get_l_2(self, t=0) -> Mobject:
        start = [-4, np.sin(t) * 3 * pi / 7, 0]
        old_start = [-4, 0, 0]
        end = [np.sin(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7 - 4, np.cos(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7, 0]
        return Line(
            start,
            [start[0] + (end[0] - old_start[0]), start[1] + (end[1] - old_start[1]), 0],
            color=RED,
        )

    def get_l_3(self, t=0) -> Mobject:
        start = [
            -4 + ((np.sin(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7 - 4) + 4),
            np.sin(t) * 3 * pi / 7 + ((np.cos(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7)),
            0,
        ]
        old_start = [-4, 0, 0]
        end = [np.sin(4 / 3 * pi) * np.sin(t + 4 / 3 * pi) * 3 * pi / 7 - 4, np.cos(4 / 3 * pi) * np.sin(t + 4 / 3 * pi) * 3 * pi / 7, 0]
        return Line(
            start,
            [start[0] + (end[0] - old_start[0]), start[1] + (end[1]), 0],
            color=GREEN
        )
    def get_l_4(self, t =0) -> Mobject:
        start = [
            -4 + ((np.sin(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7 - 4) + 4),
            np.sin(t) * 3 * pi / 7 + ((np.cos(2 / 3 * pi) * np.sin(t + 2 / 3 * pi) * 3 * pi / 7)),
            0,
        ]
        old_start = [-4, 0, 0]
        end = [np.sin(4 / 3 * pi) * np.sin(t + 4 / 3 * pi) * 3 * pi / 7 - 4, np.cos(4 / 3 * pi) * np.sin(t + 4 / 3 * pi) * 3 * pi / 7, 0]
        return Line(
            [-4,0,0],
            [start[0] + (end[0] - old_start[0]), start[1] + (end[1]), 0],
            color=GREY_B
        )

    def construct(self):
        f_1 = self.get_sine_wave(amplitude=2)
        f_2 = self.get_sine_wave(amplitude=2, color=RED)
        f_3 = self.get_sine_wave(amplitude=2, color=GREEN)

        c_1 = self.get_c_1()
        c_2 = self.get_c_2()
        c_3 = self.get_c_3()

        l_1 = self.get_l_1()
        l_2 = self.get_l_2()
        l_3 = self.get_l_3()
        l_4 = self.get_l_4()

        d_theta = ValueTracker(0)

        def update_wave_1(func):
            func.become(self.get_sine_wave(dx=d_theta.get_value() * 0.3, amplitude=2))
            return func

        def update_wave_2(func):
            func.become(self.get_sine_wave(dx=d_theta.get_value() * 0.3 + 2 / 3 * pi, amplitude=2, color=RED))
            return func

        def update_wave_3(func):
            func.become(self.get_sine_wave(dx=d_theta.get_value() * 0.3 + 4 / 3 * pi, amplitude=2, color=GREEN))
            return func

        def update_c_1(func):
            func.become(self.get_c_1(t=d_theta.get_value() * 0.3))
            return func

        def update_c_2(func):
            func.become(self.get_c_2(t=d_theta.get_value() * 0.3))
            return func

        def update_c_3(func):
            func.become(self.get_c_3(t=d_theta.get_value() * 0.3))
            return func

        def update_l_1(func):
            func.become(self.get_l_1(t=d_theta.get_value() * 0.3))
            return func

        def update_l_2(func):
            func.become(self.get_l_2(t=d_theta.get_value() * 0.3))
            return func

        def update_l_3(func):
            func.become(self.get_l_3(t=d_theta.get_value() * 0.3))
            return func
        
        def update_l_4(func):
            func.become(self.get_l_4(t=d_theta.get_value() * 0.3))
            return func

        grid = Axes(
            x_length=6,
            y_length=4,
            x_range=[0.0, pi * 6, pi],
            y_range=[-2.0, 2.0, 0.5],
            tips=False,
        ).set_x(3)

        title = Title(
            r"Rotierende Magnetfelder",
            include_underline=False,
            font_size=52,
        )

        f_1.add_updater(update_wave_1)
        f_2.add_updater(update_wave_2)
        f_3.add_updater(update_wave_3)

        c_1.add_updater(update_c_1)
        c_2.add_updater(update_c_2)
        c_3.add_updater(update_c_3)

        l_1.add_updater(update_l_1)
        l_2.add_updater(update_l_2)
        l_3.add_updater(update_l_3)
        l_4.add_updater(update_l_4)

        self.add(Rectangle(color=WHITE, height=5, width=7).set_x(3).set_y(0))
        self.add(Circle(radius=2, color=WHITE, stroke_width=5).set_x(-4).set_y(0), c_1, c_2, c_3)
        self.add(f_1, f_2, f_3, title, grid, l_1, l_2, l_3, l_4)
        self.play(d_theta.animate(rate_func=linear).increment_value(20 * PI), rate_func=linear, run_time=10)
