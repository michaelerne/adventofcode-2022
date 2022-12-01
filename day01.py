from run_util import run_puzzle


def part_a(data):
    elfes = [x for x in data.split('\n\n')]
    calories = []
    for elf in elfes:
        calories.append(sum([int(x) for x in elf.split('\n')]))
    return max(calories)


def part_b(data):
    elfes = [x for x in data.split('\n\n')]
    calories = []
    for elf in elfes:
        calories.append(sum([int(x) for x in elf.split('\n')]))
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
