from heapq import heappop, heappush

from run_util import run_puzzle

D_X = [-1, 0, 1, 0]
D_Y = [0, -1, 0, 1]
D_XY = list(zip(D_X, D_Y))


def get_neighbors(grid, x, y):
    return [
        (x + dx, y + dy)
        for dx, dy in D_XY if (x + dx, y + dy) in grid
    ]


def parse_data(data):

    grid = {
        (x, y): ord(cell)
        for y, line in enumerate(data.split('\n'))
        for x, cell in enumerate(line)
    }

    start, end = None, None
    for point in grid.keys():
        if grid[point] == ord('S'):
            start = point
            grid[start] = ord('a')
        elif grid[point] == ord('E'):
            end = point
            grid[end] = ord('z')

    return grid, start, end


def get_shortest_path(grid, start, end):
    queue = [(0, start)]

    costs = {}

    while queue:
        cost, point = heappop(queue)
        if point == end:
            return cost

        for neighbor in get_neighbors(grid, *point):

            if grid[neighbor] - grid[point] > 1:
                continue

            neighbor_cost = cost + 1
            if neighbor in costs and costs[neighbor] <= neighbor_cost:
                continue
            costs[neighbor] = neighbor_cost
            heappush(queue, (neighbor_cost, neighbor))

    return float('inf')


def part_a(data):
    grid, start, end = parse_data(data)

    answer = get_shortest_path(grid, start, end)

    return answer


def part_b(data):
    grid, start, end = parse_data(data)

    answer = min([get_shortest_path(grid, point, end) for point, height in grid.items() if height == ord('a')])

    return answer


def main():
    examples = [
        ("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""", 31, 29)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
