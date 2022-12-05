from run_util import run_puzzle
from parse import parse

def part_a(data):
    field_text, instruction_text = data.split('\n\n')
    field_lines = field_text.split('\n')
    stacks = [[] for _ in range(len(field_lines[0])//4 + 1)]
    for line in reversed(field_lines[0:-1]):
        for stack, crate in enumerate([line[char] for char in range(1, len(line), 4)]):
            if crate == ' ':
                continue
            else:
                stacks[stack].append(crate)

    instructions = [parse("move {:d} from {:d} to {:d}", line) for line in instruction_text.split('\n')]

    for number_of_crates, source_stack, destination_stack in instructions:
        for _ in range(number_of_crates):
            moving_crate = stacks[source_stack-1].pop()
            stacks[destination_stack-1].append(moving_crate)

    solution = ''.join([stack[-1] for stack in stacks])
    return solution


def part_b(data):
    field_text, instruction_text = data.split('\n\n')
    field_lines = field_text.split('\n')
    stacks = [[] for _ in range(len(field_lines[0])//4 + 1)]
    for line in reversed(field_lines[0:-1]):
        for stack, crate in enumerate([line[char] for char in range(1, len(line), 4)]):
            if crate == ' ':
                continue
            else:
                stacks[stack].append(crate)

    instructions = [parse("move {:d} from {:d} to {:d}", line) for line in instruction_text.split('\n')]

    for number_of_crates, source_stack, destination_stack in instructions:
        moving_crate = stacks[source_stack-1][-1 * number_of_crates:]
        del stacks[source_stack-1][-1 * number_of_crates:]
        stacks[destination_stack-1] += moving_crate

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
