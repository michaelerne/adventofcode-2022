import collections
from itertools import count

from run_util import run_puzzle

ROCKS = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(2, 0), (2, 1), (3, 0), (3, 1)],
]

WIDTH = 7


def run_sim(instructions, tower=None, start_rock_idx=0, jet_idx=0):
    if tower is None:
        tower = set((x, 0) for x in range(WIDTH))

    rock_len = len(ROCKS)
    jet_len = len(instructions)

    for rock_idx in count(start_rock_idx):
        rock = ROCKS[rock_idx % 5]
        y_off = max(y for x, y in tower) + 4
        rock = {(x, y + y_off) for x, y in rock}

        start_ids = (rock_idx % rock_len, jet_idx % jet_len)
        total_d_x, total_d_y = 0, 0

        while True:
            d_x = -1 if instructions[jet_idx % jet_len] == '<' else 1
            jet_idx += 1

            new_rock = {(x + d_x, y) for x, y in rock}
            if all(0 <= x < WIDTH for x, _y in new_rock):
                if len(new_rock.intersection(tower)) == 0:
                    # move rock left/right
                    rock = new_rock
                    total_d_x += 1

            new_rock = {(x, y - 1) for x, y in rock}
            if len(new_rock.intersection(tower)) > 0:
                # rock would collide therefore it has settled
                tower.update(rock)

                current_height = max(y for x, y in tower)

                layout = tuple(
                    max(y - current_height for x, y in tower if x == tx)
                    for tx in range(WIDTH)
                )

                key = (start_ids, total_d_x, total_d_y)
                state = (current_height, rock_idx, layout, key, tower)
                yield state
                break

            # move rock down
            rock = new_rock
            total_d_y -= 1


def part_a(data):
    sim = run_sim(data)

    # fast-forward
    for _ in range(2021):
        next(sim)

    current_height, *_ = next(sim)

    return current_height


def part_b(data):
    sim = run_sim(data)

    total_steps = 1_000_000_000_000

    tower_heights = collections.defaultdict(list)

    for current_height, rock_idx, layout, key, tower in sim:
        info_for_move = tower_heights[key]
        if len(info_for_move) > 1:
            prev_1, prev_2 = info_for_move[-1], info_for_move[-2]
            prev_1_height, prev_2_height = prev_1[0], prev_2[0]
            prev_1_rock_idx, prev_2_rock_idx = prev_1[1], prev_2[1]

            last_height_diff = prev_1_height - prev_2_height
            curr_height_diff = current_height - prev_1_height

            last_rock_idx_diff = prev_1_rock_idx - prev_2_rock_idx
            curr_rock_idx_diff = rock_idx - prev_1_rock_idx

            if curr_height_diff == last_height_diff and last_rock_idx_diff == curr_rock_idx_diff:
                steps_remaining = total_steps - rock_idx - 1

                cycle_length = rock_idx - prev_1_rock_idx
                cycles = steps_remaining // cycle_length
                skip_steps = cycles * cycle_length

                # fast-forward
                steps_remaining = total_steps - (rock_idx + 1 + skip_steps)
                for _ in range(steps_remaining - 1):
                    next(sim)

                *_, tower = next(sim)

                return max(y for x, y in tower) + curr_height_diff * cycles

        info_for_move.append((current_height, rock_idx, layout))


def main():
    examples = [
        (""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 3068, 1514285714288)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, None, part_b, examples)


if __name__ == '__main__':
    main()
