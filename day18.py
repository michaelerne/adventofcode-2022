from run_util import run_puzzle
from collections import deque

D_XYZ = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def parse_data(data):
    return {tuple([int(i) for i in line.split(',')]) for line in data.split('\n')}


def neighbors(point):
    x, y, z = point
    for d_x, d_y, d_z in D_XYZ:
        yield x + d_x, y + d_y, z + d_z


def empty_points(cubes):
    x_values, y_values, z_values = zip(*cubes)
    grid = {
        (x, y, z)
        for x in range(min(x_values) - 1, max(x_values) + 2)
        for y in range(min(y_values) - 1, max(y_values) + 2)
        for z in range(min(z_values) - 1, max(z_values) + 2)
    }
    empty = grid.difference(cubes)

    queue = [(min(x_values) - 1, min(y_values) - 1, min(z_values) - 1)]

    while queue:
        point = queue.pop()
        if point in empty:
            empty.remove(point)
            queue.extend(neighbors(point))

    return empty


def part_a(data):
    cubes = parse_data(data)

    seen = set()
    sides = 0
    for cube in cubes:
        sides += 6
        for neighbor in neighbors(cube):
            if neighbor in seen:
                sides -= 2
        seen.add(cube)

    return sides


def part_b(data):
    cubes = parse_data(data)

    empty = empty_points(cubes)

    seen = set()

    sides = 0
    for cube in cubes:
        sides += 6
        for neighbor in neighbors(cube):
            if neighbor in seen:
                sides -= 2
            elif neighbor in empty:
                sides -= 1
        seen.add(cube)

    return sides


def main():
    examples = [
        ("""1,1,1
2,1,1""", 10, 10),
        ("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""", 64, 58)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
