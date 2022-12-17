import math

from parse import parse

from run_util import run_puzzle
from itertools import product

def distance(s_x, s_y, b_x, b_y):
    return abs(s_x - b_x) + abs(s_y - b_y)


def parse_data(data):
    tokens = [parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
              for line in data.split('\n')]
    data = {
        (s_x, s_y): distance(s_x, s_y, b_x, b_y)
        for s_x, s_y, b_x, b_y in tokens
    }

    return data


def part_a(data):
    radius = parse_data(data)

    y_target = 20 if radius.get((2, 18), None) == 7 else 2_000_000

    x_min = math.inf
    x_max = -math.inf
    for (s_x, s_y), s_distance in radius.items():
        d_x = s_distance - abs(y_target - s_y)
        if d_x > 0:
            x_min = min(x_min, s_x - d_x)
            x_max = max(x_max, s_x + d_x)

    return x_max - x_min


def part_b(data):

    radius = parse_data(data)
    scanners = radius.keys()

    pos_gradient, neg_gradient = set(), set()
    for ((x, y), r) in radius.items():
        pos_gradient.add(y - x + r + 1)
        pos_gradient.add(y - x - r - 1)
        neg_gradient.add(x + y + r + 1)
        neg_gradient.add(x + y - r - 1)

    boundary = 4_000_000
    for a, b in product(pos_gradient, neg_gradient):
        intersection = ((b - a) // 2, (a + b) // 2)
        if all(0 < dimension < boundary for dimension in intersection):
            if all(distance(*intersection, *target) > radius[target] for target in scanners):
                return 4_000_000 * intersection[0] + intersection[1]

    # sensors = [
    #     (s_x, s_y, b_x, b_y)
    #     for s_x, s_y, b_x, b_y in findall("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}\n", data)
    # ]
    #
    # boundary = 20 if sensors[0] == (2, 18, -2, 15) else 4_000_000
    #
    # def dist(s_x, s_y, b_x, b_y):
    #     return abs(s_x - b_x) + abs(s_y - b_y)
    #
    # def intersect(coord_sum, coord_dif):
    #     x = (coord_sum + coord_dif) // 2
    #     y = coord_sum - x
    #     return x, y
    #
    # def answer(x, y):
    #     return (
    #             x in range(boundary + 1) and y in range(boundary + 1) and
    #             all(dist(sx, sy, x, y) > dist(sx, sy, bx, by) for sx, sy, bx, by in sensors)
    #     )
    #
    # def get_answer(x, y):
    #     return x * 4000000 + y
    #
    # def main(sx, sy, bx, by):
    #     r = dist(sx, sy, bx, by) + 1
    #     return sx + sy + r, sx + sy - r
    #
    # def off(sx, sy, bx, by):
    #     r = dist(sx, sy, bx, by) + 1
    #     return sx - sy + r, sx - sy - r
    #
    # for s1 in sensors:
    #     for s2 in sensors:
    #         for m in main(*s1):
    #             for o in off(*s2):
    #                 p = intersect(m, o)
    #                 if answer(*p):
    #                     return get_answer(*p)
    #         for o in off(*s1):
    #             for m in main(*s2):
    #                 p = intersect(o, m)
    #                 if answer(*p):
    #                     return get_answer(*p)


def main():
    examples = [
        ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 26, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
