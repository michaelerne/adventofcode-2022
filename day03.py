from run_util import run_puzzle


def get_priority(item: str):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

def part_a(data):
    input = [[*line] for line in data.split('\n')]

    score = 0
    for line in input:
        left, right = set(line[0:len(line)//2]), set(line[len(line)//2:])
        (common,) = left.intersection(right)
        score += get_priority(common)
    return score

def part_b(data):
    input = [[*line] for line in data.split('\n')]
    groups = list(zip(input[0::3], input[1::3], input[2::3]))

    score = 0
    for group in groups:
        (common,) = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        score += get_priority(common)
    return score


def main():
    examples = [
        ("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""", 157, 70)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
