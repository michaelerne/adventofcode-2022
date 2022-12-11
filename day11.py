from dataclasses import dataclass
from math import prod
from typing import List, Callable

from parse import findall, parse

from run_util import run_puzzle


@dataclass
class Monkey:
    items: List[int]
    inspect: Callable[[int], int]
    operation: Callable[[int], int]
    divisor: int
    destination: Callable[[int], int]

    inspected: int = 0

    def ook(self):
        self.inspected += len(self.items)
        for item in self.items:
            item = self.operation(item)
            item = self.inspect(item)
            yield self.destination(item), item
        self.items = []


def go_bananas(monkeys: List[Monkey], rounds):
    for _ in range(rounds):
        for monkey in monkeys:
            for target, item in monkey.ook():
                monkeys[target].items.append(item)
    inspection_counts: List[int] = sorted([monkey.inspected for monkey in monkeys])
    return inspection_counts[-2] * inspection_counts[-1]


def parse_monkeys(data: str, relaxed: bool) -> List[Monkey]:
    monkeys: List[Monkey] = []
    for monkey in data.split('\n\n'):
        _index, items, operation, test, true, false = [line.strip() for line in monkey.split('\n')]

        items = [item[0] for item in findall("{:d}", items)]

        inspect = lambda x: x // 3

        op, value = parse("Operation: new = old {} {}", operation)
        match (op, value):
            case ('*', 'old'):
                operation = lambda x: x * x
            case ('*', value):
                operation = (lambda value: lambda x: x * value)(int(value))
            case ('+', value):
                operation = (lambda value: lambda x: x + value)(int(value))

        divisor, = parse("Test: divisible by {:d}", test)
        true, = parse("If true: throw to monkey {:d}", true)
        false, = parse("If false: throw to monkey {:d}", false)
        destination = (lambda divisor, true, false: lambda x: true if x % divisor == 0 else false)(divisor, true, false)

        monkeys.append(Monkey(items, inspect, operation, divisor, destination))

    if relaxed:
        product = prod([monkey.divisor for monkey in monkeys])
        for idx in range(len(monkeys)):
            monkeys[idx].inspect = (lambda product: lambda x: x % product)(product)

    return monkeys


def part_a(data):
    monkeys = parse_monkeys(data, relaxed=False)
    return go_bananas(monkeys, 20)


def part_b(data):
    monkeys = parse_monkeys(data, relaxed=True)
    return go_bananas(monkeys, 10000)


def main():
    examples = [
        ("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""", 10605, 2713310158)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
