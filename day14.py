from itertools import count

from run_util import run_puzzle

D_XY = [(0, 1), (-1, 1), (1, 1)]


def parse_data(data):
    lines = [
        [
            tuple(int(axis) for axis in position.split(','))
            for position in line.split(' -> ')
        ]
        for line in data.strip().split('\n')
    ]

    grid = {
        (x, y)
        for line in lines
        for (x1, y1), (x2, y2) in zip(line, line[1:])
        for y in range(min(y1, y2), max(y1, y2) + 1)
        for x in range(min(x1, x2), max(x1, x2) + 1)
    }

    return grid


def simulate_sand(grid):
    start_position = (500, 0)

    lowest_x = max(position[1] for position in grid)

    for sand_count in count():
        x, y = start_position
        while True:
            if y > lowest_x:  # falling into the endless void
                return sand_count
            elif (x, y + 1) not in grid:  # down one step
                x, y = x, y + 1
                continue
            elif (x - 1, y + 1) not in grid:  # one step down and to the left
                x, y = x - 1, y + 1
                continue
            elif (x + 1, y + 1) not in grid:  # one step down and to the right
                x, y = x + 1, y + 1
                continue
            else:
                grid.add((x, y))
                break

        if (x, y) == start_position:  # source of the sand becomes blocked
            return sand_count + 1


def part_a(data):
    grid = parse_data(data)

    answer = simulate_sand(grid)

    return answer


def part_b(data):
    grid = parse_data(data)

    floor = 2 + max(r[1] for r in grid)
    x_min = min(r[0] for r in grid) - floor
    x_max = max(r[0] for r in grid) + floor
    grid.update((x, floor) for x in range(x_min, x_max))
    answer = simulate_sand(grid)

    return answer


def main():
    examples = [
        ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 24, 93)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
