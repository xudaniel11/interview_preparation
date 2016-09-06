"""
Construct an H-tree, given its center (x and y coordinates), starting_length
and depth. You can assume that you have a drawLine method.

An H-tree can be constructed by starting with a line segment of arbitrary
length, drawing two segments of the same length at right angles to the
first through its endpoints, and continuing in the same vein, reducing (dividing)
the length of the line segments drawn at each stage by √2.
"""


def draw_line(start_coordinate, end_coordinate):
    # pretend this exists
    return


def construct_htree(coordinate, length, depth):
    if depth == 0:
        return

    x = coordinate.x
    y = coordinate.y

    top_left = Coordinate(x - length / 2, y + length / 2)
    mid_left = Coordinate(x - length / 2, y)
    bottom_left = Coordinate(x - length / 2, y - length / 2)
    top_right = Coordinate(x + length / 2, y + length / 2)
    mid_right = Coordinate(x + length / 2, y)
    bottom_right = Coordinate(x + length / 2, y - length / 2)

    draw_line(top_left, bottom_left)
    draw_line(mid_left, mid_right_)
    draw_line(top_right, bottom_right)

    length = length / (2**0.5)

    construct_htree(top_left, length, depth - 1)
    construct_htree(bottom_left, length, depth - 1)
    construct_htree(top_right, length, depth - 1)
    construct_htree(bottom_right, length, depth - 1)


class Coordinate():

    def __init__(self, x_arg, y_arg):
        self.x = x_arg
        self.y = y_arg
