from run_util import run_puzzle

D_X = [(-1, 0), (1, 0)]
D_Y = [(0, -1), (0, 1)]
D_XY = D_X + D_Y


def part_a(data):
    grid = [[int(char) for char in line] for line in data.strip().split('\n')]

    x_max = len(grid)
    y_max = len(grid[0])

    def is_visible(x, y):
        for d_x, d_y in D_XY:
            n_x, n_y = x + d_x, y + d_y

            while 0 <= n_x < x_max and 0 <= n_y < y_max and grid[n_x][n_y] < grid[x][y]:
                n_x += d_x
                n_y += d_y

            if not (0 <= n_x < x_max and 0 <= n_y < y_max):
                return True

        return False

    count = sum([is_visible(x, y) for x in range(x_max) for y in range(y_max)])

    return count


def part_b(data):
    grid = [[int(char) for char in line] for line in data.strip().split('\n')]

    x_max = len(grid)
    y_max = len(grid[0])

    def get_scenic_score(x, y):
        scenic_score = 1
        for d_x, d_y in D_XY:
            direction_score = 0
            n_x, n_y = x + d_x, y + d_y

            while 0 <= n_x < x_max and 0 <= n_y < y_max:
                direction_score += 1

                if grid[n_x][n_y] >= grid[x][y]:
                    break

                n_x += d_x
                n_y += d_y

            scenic_score *= direction_score

        return scenic_score

    best_score = max([get_scenic_score(x, y) for x in range(x_max) for y in range(y_max)])

    return best_score


def main():
    examples = [
        ("""30373
25512
65332
33549
35390
""", 21, 8)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
