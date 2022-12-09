from parse import parse

from run_util import run_puzzle

D_X = {"U": 0, "R": 1, "D": 0, "L": -1}
D_Y = {"U": -1, "R": 0, "D": 1, "L": 0}


def simulate(data, knots):
    lines = [parse("{} {:d}", line) for line in data.split('\n')]

    visited = set()
    x = [0 for _ in range(knots)]
    y = [0 for _ in range(knots)]

    for direction, amount in lines:
        for _ in range(amount):
            x[0] += D_X[direction]
            y[0] += D_Y[direction]
            for knot_idx in range(1, knots):
                x_cur, x_prev = x[knot_idx], x[knot_idx - 1]
                y_cur, y_prev = y[knot_idx], y[knot_idx - 1]
                if abs(x_cur - x_prev) > 1 or abs(y_cur - y_prev) > 1:
                    x[knot_idx] += (x_prev > x_cur) - (x_prev < x_cur)
                    y[knot_idx] += (y_prev > y_cur) - (y_prev < y_cur)
            visited.add((x[-1], y[-1]))

    return len(visited)


def part_a(data):
    return simulate(data, 2)


def part_b(data):
    return simulate(data, 10)


def main():
    examples = [
        ("""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""", 13, 1),
        ("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""", None, 36)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
