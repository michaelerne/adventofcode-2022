from collections import deque

from run_util import run_puzzle


def mix(data, times=1, decryption_key=1):

    # map the values to something unique for `.index()`
    values = {index: number for index, number in enumerate([int(line) * decryption_key for line in data.split('\n')])}
    file = deque(values.keys())
    order = list(values.keys())

    for _ in range(times):
        for number in order:

            # rotate and remove number
            idx = file.index(number)
            file.rotate(-1 * idx)
            file.popleft()

            # rotate by the value
            file.rotate(-1 * values[number])

            # add number back in
            file.insert(0, number)

    # transform back to proper values
    file = [values[index] for index in file]

    zero_idx = file.index(0)
    return sum(
        file[(zero_idx + off) % len(file)]
        for off in (1000, 2000, 3000)
    )


def part_a(data):
    answer = mix(data)

    return answer


def part_b(data):
    answer = mix(data, 10, decryption_key=811589153)

    return answer


def main():
    examples = [
        ("""1
2
-3
3
-2
0
4""", 3, 1623178306)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
