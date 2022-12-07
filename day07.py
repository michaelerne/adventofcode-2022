from collections import defaultdict

from run_util import run_puzzle


def parse_input(data):
    lines = data.split('\n')

    current_dir = []
    dirs = defaultdict(int)

    for line in lines:
        match line.split(' '):
            case ["$", "cd", path] if path == '/':
                current_dir = ['/']
            case ["$", "cd", path] if path == '..':
                if current_dir != ['/']:
                    current_dir = current_dir[:-1]
            case ["$", "cd", path]:
                current_dir += [path]
            case ["$", "ls"]:
                continue
            case ["dir", _dir_name]:
                continue
            case [size, _file_name]:
                for end in range(len(current_dir)):
                    dirs['/' + '/'.join(current_dir[1:end + 1])] += int(size)

    return dirs


def part_a(data):
    dirs = parse_input(data)

    score = sum([size for size in dirs.values() if size <= 100000])

    return score


def part_b(data):
    dirs = parse_input(data)

    free_pending = 30000000 - (70000000 - dirs['/'])

    score = sorted([size for size in dirs.values() if size >= free_pending])[0]

    return score


def main():
    examples = [
        ("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 95437, 24933642)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
