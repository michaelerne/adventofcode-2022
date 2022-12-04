from parse import *

from run_util import run_puzzle


def part_a(data):
    assignments = [parse("{:d}-{:d},{:d}-{:d}", x) for x in data.split('\n')]
    score = 0
    for left_start, left_end, right_start, right_end in assignments:
        left, right = set(range(left_start, left_end + 1)), set(range(right_start, right_end + 1))
        if left.issubset(right) or right.issubset(left):
            score += 1
    return score


def part_b(data):
    assignments = [parse("{:d}-{:d},{:d}-{:d}", x) for x in data.split('\n')]
    score = 0
    for left_start, left_end, right_start, right_end in assignments:
        left, right = set(range(left_start, left_end + 1)), set(range(right_start, right_end + 1))
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
