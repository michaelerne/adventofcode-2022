from parse import parse

from run_util import run_puzzle


def parse_input(data):
    field_text, instruction_text = data.split('\n\n')
    field_lines = field_text.split('\n')
    stacks = [[] for _ in range(len(field_lines[0]) // 4 + 1)]
    for line in field_lines[-2::-1]:
        for stack, crate in enumerate([line[char] for char in range(1, len(line), 4)]):
            if crate == ' ':
                continue
            else:
                stacks[stack].append(crate)

    instructions = [
        (number_of_crates, source_stack - 1, destination_stack - 1)
        for number_of_crates, source_stack, destination_stack in
        [
            parse("move {:d} from {:d} to {:d}", line)
            for line in instruction_text.split('\n')
        ]
    ]
    return stacks, instructions


def part_a(data):
    stacks, instructions = parse_input(data)

    for number_of_crates, source_stack, destination_stack in instructions:
        moving_crates = [stacks[source_stack].pop() for _ in range(number_of_crates)]
        stacks[destination_stack].extend(moving_crates)

    solution = ''.join([stack[-1] for stack in stacks])
    return solution


def part_b(data):
    stacks, instructions = parse_input(data)

    for number_of_crates, source_stack, destination_stack in instructions:
        moving_crates = [stacks[source_stack].pop() for _ in range(number_of_crates)]
        stacks[destination_stack].extend(reversed(moving_crates))

    solution = ''.join([stack[-1] for stack in stacks])
    return solution


def main():
    examples = [
        ("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""", "CMZ", "MCD")
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
