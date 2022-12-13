import json
from functools import cmp_to_key
from math import prod

from run_util import run_puzzle


def parse_data(data):
    pairs = [pair.split('\n') for pair in data.strip().split('\n\n')]

    pairs = [(json.loads(left), json.loads(right)) for left, right in pairs]
    return pairs


def compare(left, right):
    left_len, right_len = len(left), len(right)
    for index in range(min(left_len, right_len)):
        left_item, right_item = left[index], right[index]

        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item < right_item:
                return True
            if left_item > right_item:
                return False
            continue

        elif isinstance(left_item, list) and isinstance(right_item, list):
            result = compare(left_item, right_item)
            if result is not None:
                return result
            continue

        if isinstance(left_item, int):
            left_item = [left_item]
        elif isinstance(right_item, int):
            right_item = [right_item]

        result = compare(left_item, right_item)
        if result is not None:
            return result
    if left_len < right_len:
        return True
    if left_len > right_len:
        return False


def part_a(data):
    pairs = parse_data(data)

    return sum([index for index, (left, right) in enumerate(pairs, start=1) if compare(left, right)])


def part_b(data):
    pairs = parse_data(data)
    packets = [packet for pair in pairs for packet in pair]
    divider_packets = [[[2]], [[6]]]
    packets += divider_packets

    sorted_packets = sorted(packets, key=cmp_to_key(lambda left, right: -1 if compare(left, right) else 1))

    answer = prod([sorted_packets.index(divider_packet) + 1 for divider_packet in divider_packets])

    return answer


def main():
    examples = [
        ("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""", 13, 140)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
