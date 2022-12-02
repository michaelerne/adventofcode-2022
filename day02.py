from run_util import run_puzzle


def part_a(data):
    games = [line.split(' ') for line in data.split('\n')]

    move_score = {'X': 1, 'Y': 2, 'Z': 3}
    result_score = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                    ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                    ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}

    score = sum([move_score[my_move] + result_score[(op_move, my_move)] for op_move, my_move in games])
    return score


def part_b(data):
    games = [line.split(' ') for line in data.split('\n')]

    move_score = {'X': 0, 'Y': 3, 'Z': 6}
    result_score = {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                    ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                    ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}

    score = sum([move_score[my_move] + result_score[(op_move, my_move)] for op_move, my_move in games])
    return score


def main():
    examples = [
        ("""A Y
B X
C Z""", 15, 12)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
