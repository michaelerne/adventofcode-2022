from typing import List

from run_util import run_puzzle


def parse_data(data) -> List[int]:
    elfes = [chunk for chunk in data.split('\n\n')]
    calories = [sum([int(line) for line in elf.split('\n')]) for elf in elfes]
    return calories


def part_a(data):
    calories = parse_data(data)
    return max(calories)


def part_b(data):
    calories = parse_data(data)
    return sum(sorted(calories, reverse=True)[0:3])


def main():
    examples = [
        ("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""", 24000, 45000)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
