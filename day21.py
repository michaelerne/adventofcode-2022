from functools import cache

import sympy

from run_util import run_puzzle


def parse_data(data):
    monkeys = [line.strip().split(": ") for line in data.split('\n')]
    monkeys = {monkey: job.split(' ') for monkey, job in monkeys}
    return monkeys


def part_a(data):
    monkeys = parse_data(data)

    @cache
    def solve(monkey_name):
        monkey = monkeys[monkey_name]
        if len(monkey) == 1:
            return monkey[0]

        monkey_a, op, monkey_b = monkey
        return f"({solve(monkey_a)}) {op} ({solve(monkey_b)})"

    expr = solve('root')
    answer = sympy.parse_expr(expr)
    return answer


def part_b(data):
    monkeys = [line.strip().split(": ") for line in data.split('\n')]
    monkeys = {monkey: job.split(' ') for monkey, job in monkeys}

    @cache
    def solve(monkey_name):
        if monkey_name == 'humn':
            return 'x'

        monkey = monkeys[monkey_name]
        if len(monkey) == 1:
            return monkey[0]

        monkey_a, op, monkey_b = monkey
        return f"({solve(monkey_a)}) {op} ({solve(monkey_b)})"

    eq_a = solve(monkeys['root'][0])
    eq_b = solve(monkeys['root'][2])

    x = sympy.symbols('x')
    eq_a = sympy.parse_expr(eq_a, local_dict={'x': x})
    eq_b = sympy.parse_expr(eq_b, local_dict={'x': x})

    answer = sympy.solve(sympy.Eq(eq_a, eq_b))[0]
    return answer


def main():
    examples = [
        ("""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""", 152, 301)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
