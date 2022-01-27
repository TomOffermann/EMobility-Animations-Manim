from manim import *


def circle_with_text(
    r: int, txt: str, color=BLACK, font_size: int = 10, font_color=BLACK, stroke_width: int = 2, fill_color=BLACK
) -> Mobject:
    c = Circle(r, color).set_opacity(1).set_fill(fill_color)
    t = Tex(txt, stroke_width=stroke_width, font_size=font_size, color=font_color)
    return VGroup(c, t)


def electron() -> Mobject:
    return circle_with_text(0.15, "e$^-$", YELLOW_D, 24, BLACK, 1, YELLOW_D)


def oxygen() -> Mobject:
    list = []
    start = 0.3
    end = 0.6
    list.append(Line(start=LEFT * start, end=LEFT * end))
    list.append(Line(start=RIGHT * start, end=RIGHT * end))
    list.append(Line(start=UP * start, end=UP * end))
    list.append(Line(start=DOWN * start, end=DOWN * end))
    list = map(lambda x: x.set_opacity(0.7), list)
    return VGroup(circle_with_text(0.285, "O$^2$", GREY_B, 25, WHITE, 1), *list)


def metal() -> Mobject:
    return circle_with_text(0.285, "Co", BLUE_D, 25, WHITE, 1)


def positive() -> Mobject:
    return circle_with_text(0.25, "+", RED_A, 32, BLACK, 4, RED_A)


def negative() -> Mobject:
    return circle_with_text(0.25, "-", BLUE_A, 32, BLACK, 4, BLUE_A)


def metal_oxid(rows: int, cols: int, scale=1.5) -> Mobject:
    list = []
    for i in range(rows):
        for j in range(cols):
            if (j + i) % 2 == 0:
                list.append(oxygen().set_x(i / scale).set_y(j / scale))
            else:
                list.append(metal().set_x(i / scale).set_y(j / scale))
    return VGroup(*list).set_x(0).set_y(0)


def lithium_grid(rows, cols) -> Mobject:
    list = []
    for i in range(rows):
        for j in range(cols):
            list.append(lithium_ion().set_x(j).set_y(i))
    return VGroup(*list).set_x(0).set_y(0)

def carbon_grid(rows: int) -> Mobject:
    list = []
    for i in range(rows):
        list.append(carbon_layer().set_y(i * 1.5))
    return VGroup(*list).set_x(0).set_y(0)


def carbon(small: int = False) -> Mobject:
    return circle_with_text(
        0.285 if small == 0 else (0.225 if small == 1 else 0.25),
        "C",
        GRAY_B,
        30 if small == 0 else (24 if small == 1 else 27),
        WHITE,
        1,
    ).set_z_index(5 if small == 1 else 10)


def carbon_layer() -> Mobject:
    list = []
    positions = [
        [-1.2, 0, 0],
        [-0.45, 0.4, 0],
        [0.45, 0.4, 0],
        [1.2, 0, 0],
        [0.55, -0.3, 0],
        [-0.55, -0.3, 0],
    ]
    small = [2, 1, 1, 2, 0, 0]
    for i in range(len(positions)):
        list.append(Line(positions[i], positions[i - 1], color=GREY_B).set_z_index(4))
        list.append(carbon(small[i]).set_x(positions[i][0]).set_y(positions[i][1]))
    list.append(Polygon(*positions, color=WHITE).set_fill(WHITE, 0.075).set_z_index(-1))
    return VGroup(*list)


def lithium_ion() -> Mobject:
    return circle_with_text(0.285, "Li$^+$", RED_D, 25, WHITE, 1)


def move_along_complex_path(obj: Mobject, stop_indices, points, run_time: float, rate_func=linear):
    animations = []
    paths = []
    for i in range(len(points) - 1):
        if i not in stop_indices:
            paths.append(Line(points[i], points[i + 1]))

    for i in range(len(paths)):
        animations.append(MoveAlongPath(obj, paths[i], run_time=run_time, rate_func=rate_func))

    return animations
