# Solution for Problem 1 Day 22 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day22-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day22-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------

# Possible moves
movements = ((1, 0), (0, 1), (-1, 0), (0, -1))


# Step around the map
def step(new_x: int, new_y: int, move: int, row_limits: list, col_limits: list) -> (int, int):
    delta = movements[move]

    # Wrap horizontal move
    if move in [0, 2]:
        new_x += delta[0]
        min_x, max_x = row_limits[new_y]
        new_x = min_x if new_x >= max_x else max_x - 1 if new_x < min_x else new_x

    # Wrap vertical move
    elif move in [1, 3]:
        new_y += delta[1]
        min_y, max_y = col_limits[new_x]
        new_y = min_y if new_y >= max_y else max_y - 1 if new_y < min_y else new_y

    return new_x, new_y


def solution_day22_prob1(puzzle_in: list):
    # Parse the board and the commands
    board = puzzle_in[:-2]
    path = puzzle_in.pop(-1)
    commands = path.replace("R", " R ").replace("L", " L ").split(" ")

    # Find start and end for each row
    max_col = 0
    row_limits = []
    for row in board:
        valid = re.search(r"[.#]+", row)
        max_col = max(max_col, valid.end())
        row_limits += [(valid.start(), valid.end())]

    # Board sorted by columns
    col_board = [[] for _ in range(max_col)]
    for row in board:
        for index, item in enumerate(row):
            col_board[index] += [item]
    col_board = list(map(lambda x: ''.join(x), col_board))

    # Find start and end for each column
    col_limits = []
    for col in col_board:
        valid = re.search(r"[.#]+", col)
        col_limits += [(valid.start(), valid.end())]

    # Start position
    pos = [board[0].index("."), 0]

    # Execute all moves
    move = 0
    for order in commands:
        # Change orientation
        if order == "R":
            move += 1
        elif order == "L":
            move -= 1

        # Move forward
        else:
            move %= 4

            new_x, new_y = pos
            for _ in range(int(order)):

                new_x, new_y = step(new_x, new_y, move, row_limits, col_limits)

                # See if we collide with a wall
                if board[new_y][new_x] == "#":
                    break
                else:
                    pos = [new_x, new_y]
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + move


# Tests and Solution ---
print("Tests:")
print(solution_day22_prob1(test01))
print("\nSolution:")
print(solution_day22_prob1(puzzle))
