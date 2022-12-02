from run_util import run_puzzle


def part_a(data):
    games = [line.split(' ') for line in data.split('\n')]

    result = {("A", "X"): 1 + 3, ("A", "Y"): 2 + 6, ("A", "Z"): 3 + 0,
              ("B", "X"): 1 + 0, ("B", "Y"): 2 + 3, ("B", "Z"): 3 + 6,
              ("C", "X"): 1 + 6, ("C", "Y"): 2 + 0, ("C", "Z"): 3 + 3}

    score = sum([result[tuple(game)] for game in games])
    return score


def part_b(data):
    games = [line.split(' ') for line in data.split('\n')]

    goal_lose = {"B": "X", "C": "Y", "A": "Z"}
    goal_win = {"A": "Y", "B": "Z", "C": "X"}
    goal_draw = {"A": "X", "B": "Y", "C": "Z"}

    def get_result(op_move, my_goal):
        game_score = 0

        match my_goal:
            case "X":
                my_move = goal_lose[op_move]
                game_score += 0
            case "Y":
                my_move = goal_draw[op_move]
                game_score += 3
            case _:  # case "Z":
                my_move = goal_win[op_move]
                game_score += 6

        match my_move:
            case "X":
                game_score += 1
            case "Y":
                game_score += 2
            case "Z":
                game_score += 3

        return game_score

    score = sum([get_result(*game) for game in games])
    return score


def main():
    examples = [
        ("""A Y
B X
C Z""", 15, 12)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
