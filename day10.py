from advent_of_code_ocr import convert_6

from run_util import run_puzzle


def get_signals(data):
    lines = data.split('\n')
    signals = [1]
    for line in lines:
        match line.split(' '):
            case ['noop']:
                signals.append(signals[-1])
            case ['addx', value]:
                signals += [signals[-1], signals[-1] + int(value)]
    return signals


def part_a(data):
    signals = get_signals(data)
    return sum([signals[i - 1] * i for i in range(len(signals)) if (i - 20) % 40 == 0 and i <= 220])


def part_b(data):
    signals = get_signals(data)
    chars = ''.join([
        '#' if index % 40 in [signals[index] - 1, signals[index], signals[index] + 1] else '.'
        for index in range(6 * 40)
    ])
    output = '\n'.join([
        chars[i:i + 40] for i in range(0, len(chars), 40)
    ])
    return convert_6(output)


def main():
    examples = [
        ("""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""", 13140, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
