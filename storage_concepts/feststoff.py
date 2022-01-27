from manim import *
import sys
import os

sys.path.append(os.path.relpath("../lib/components"))
from util import *


def accessories() -> Mobject:
    r = Line(start=[-6, 2, 0], end=[-6, -3, 0], color=RED_D)
    l = Line(start=[6, 2, 0], end=[6, -3, 0], color=BLUE_D)

    rh = VGroup(
        Line(start=[-6.5, 3, 0], end=[-6.5, -0.5, 0], color=RED_D),
        Line(start=[-6, -0.5, 0], end=[-6.5, -0.5, 0], color=RED_D),
    )
    lh = VGroup(
        Line(start=[6.5, 3, 0], end=[6.5, -0.5, 0], color=BLUE_D),
        Line(start=[6, -0.5, 0], end=[6.5, -0.5, 0], color=BLUE_D),
    )

    top = VGroup(
        Line(start=[-6.5, 3, 0], end=[-1, 3, 0]).set_color([RED_A, RED_D]),
        Line(start=[6.5, 3, 0], end=[1, 3, 0]).set_color([BLUE_D, BLUE_A]),
    )

    electric = VGroup(r, l, *top, *rh, *lh)
    separator = Rectangle(color=YELLOW_C, height=5.5, width=1).set_fill(YELLOW_C, 0.4).set_y(-0.5).set_x(-2)
    lithium_part = Rectangle(color=GREY_B, height=5.5, width=3).set_fill(WHITE, 0.1).set_y(-0.5).set_x(-4)
    carbon_part = Rectangle(color=GREY_B, height=5.5, width=7).set_fill(WHITE, 0.1).set_y(-0.5).set_x(2)

    power = VGroup(
        positive().set_x(-0.75).set_y(3).set_z_index(8),
        negative().set_x(0.75).set_y(3).set_z_index(8),
    )

    return VGroup(*power, *electric, separator, lithium_part, carbon_part)


class FestStoffBatterie(Scene):
    lithium_pos = [[-2, 0], [-4, 0], [-3, -1], [-4, 1], [-2, 2], [-3, -3], [-4, -2], [-2, -2]]
    lithium_pos_next = [[3, 0.35], [1.75, -0.5], [3, -1.15], [1.75, 1], [3, 1.85], [4.25, -0.5], [1.75, -2], [3, -2.65]]

    lithium_ions = map(lambda x: lithium_ion().set_x(x[0]).set_y(x[1]).set_z_index(8), lithium_pos)
    lithium_ions_next = map(lambda x: lithium_ion().set_x(x[0]).set_y(x[1]).set_z_index(8), lithium_pos_next)
    lithium_ions_return = map(lambda x: lithium_ion().set_x(x[0]).set_y(x[1]).set_z_index(8), lithium_pos)

    electrons_pos = list(map(lambda x: [x[0] + 0.25, x[1] + 0.25, 0], lithium_pos))
    electrons = list(map(lambda x: electron().set_x(x[0] + 0.25).set_y(x[1] + 0.25).set_z_index(11), lithium_pos))

    circle_anim_pos = list(map(lambda x: Circle(0.25).set_x(x[0]).set_y(x[1] + 0.25), lithium_pos))
    circle_anim = []

    for i in range(len(lithium_pos)):
        circle_anim.append(MoveAlongPath(electrons[i], circle_anim_pos[i], run_time=2))

    def animate_loading(
        self,
        objs,
        lithium_ions,
        lithium_ions_next,
        remove: bool = True,
    ):
        x1 = 2.05
        x2 = 4.1
        y1 = 2.25
        y2 = 1.2
        delta_y = 1.5
        elec_carbon_pos = [
            [x1, y1, 0],
            [x2, y2, 0],
            [x1, y1 - delta_y, 0],
            [1.9, -3.35, 0],
            [x1, y1 - delta_y * 2, 0],
            [x2, y2 - delta_y * 2, 0],
            [x1, y1 - delta_y * 3, 0],
            [x2, y2 - delta_y * 3, 0],
        ]
        self.play(ReplacementTransform(lithium_ions, lithium_ions_next, run_time=2))
        for i in range(len(objs)):
            a = objs[i]
            b = elec_carbon_pos[i]
            anim_exec = move_along_complex_path(
                a,
                [5],
                [
                    a.get_center(),
                    [-6, a.get_y(), 0],
                    [-6, -0.5, 0],
                    [-6.5, -0.5, 0],
                    [-6.5, 3, 0],
                    [-1, 3, 0],
                    [1, 3, 0],
                    [6.5, 3, 0],
                    [6.5, -0.5, 0],
                    [6, -0.5, 0],
                    [6, b[1], 0],
                    b,
                ],
                0.1,
            )
            for i in range(len(anim_exec)):
                self.play(anim_exec[i])
            if remove:
                self.remove(a)

    def animate_using(
        self,
        objs,
        objs_pos,
        lithium_ions,
        lithium_ions_next,
        remove: bool = True,
    ):
        for i in range(len(objs)):
            a = objs[i]
            b = objs_pos[i]
            anim_exec = move_along_complex_path(
                a,
                [5],
                [
                    a.get_center(),
                    [6, a.get_y(), 0],
                    [6, -0.5, 0],
                    [6.5, -0.5, 0],
                    [6.5, 3, 0],
                    [1, 3, 0],
                    [-1, 3, 0],
                    [-6.5, 3, 0],
                    [-6.5, -0.5, 0],
                    [-6, -0.5, 0],
                    [-6, b[1], 0],
                    [b[0], b[1], 0],
                ],
                0.1,
            )
            for i in range(len(anim_exec)):
                self.play(anim_exec[i])
            if remove:
                self.remove(a)
        self.play(ReplacementTransform(lithium_ions, lithium_ions_next, run_time=2))

    def construct(self):
        self.play(Create(accessories()))
        self.play(
            Create(lithium_grid(5, 2).set_x(-4).set_y(-0.5)),
            Create(carbon_grid(4).set_y(-0.5).set_x(0.4)),
            Create(carbon_grid(4).set_y(-0.5).set_x(3.6)),
        )
        self.wait(2)
