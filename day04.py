from run_util import run_puzzle


def part_a(data):
    assignments = [x.split(',') for x in data.split('\n')]
    score = 0
    for left_assignment, right_assignment in assignments:
        left = set(range(int(left_assignment.split('-')[0]), int(left_assignment.split('-')[1]) + 1))
        right = set(range(int(right_assignment.split('-')[0]), int(right_assignment.split('-')[1]) + 1))
        if left.issubset(right) or right.issubset(left):
            score += 1
    return score


def part_b(data):
    assignments = [x.split(',') for x in data.split('\n')]
    score = 0
    for left_assignment, right_assignment in assignments:
        left = set(range(int(left_assignment.split('-')[0]), int(left_assignment.split('-')[1]) + 1))
        right = set(range(int(right_assignment.split('-')[0]), int(right_assignment.split('-')[1]) + 1))
        if left.intersection(right):
            score += 1
    return score


def main():
    examples = [
        ("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""", 2, 4)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
