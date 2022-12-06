from run_util import run_puzzle


def part_a(data):
    input = data
    buffer = []
    for index, char in enumerate(input):
        if len(buffer) >= 4:
            del buffer[0]
        buffer.append(char)
        if len(set(buffer)) == 4:
            return index + 1

def part_b(data):
    input = data
    buffer = []
    for index, char in enumerate(input):
        if len(buffer) >= 14:
            del buffer[0]
        buffer.append(char)
        if len(set(buffer)) == 14:
            return index + 1


def main():
    examples = [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
