# Solution for Problem 2 Day 22 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day22-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day22-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------

# Possible moves: RIGHT; DOWN; LEFT; UP
movements = ((1, 0), (0, 1), (-1, 0), (0, -1))

# Cube faces
cube = {
    # Cube Face: ((min_x, max_x), (min_y, max_y))
    "A": ((100, 150), (0, 50)),
    "B": ((50, 100), (0, 50)),
    "C": ((50, 100), (50, 100)),
    "D": ((50, 100), (100, 150)),
    "E": ((0, 50), (100, 150)),
    "F": ((0, 50), (150, 200))
}


# Step around the cube
def step(x: int, y: int, move: int) -> (int, int, int):
    # Determine the face we're in and it's limits
    face = "A"
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for letter in cube:
        min_x, max_x, min_y, max_y = cube[letter][0][0], cube[letter][0][1], cube[letter][1][0], cube[letter][1][1]
        if min_x <= x < max_x and min_y <= y < max_y:
            face = letter
            break

    delta = movements[move]
    new_x, new_y = x + delta[0], y + delta[1]
    print(new_x, new_y, move, face)
    # Relative NEW positions with respect to current face
    rel_x, rel_y = new_x - cube[face][0][0], new_y - cube[face][1][0]
    # print(min_x, max_x, min_y, max_y)
    if min_x <= new_x < max_x and min_y <= new_y < max_y:
        # print("Here!")
        pass
    elif new_x < min_x:
        match face:
            case "B":
                new_x = cube["E"][0][0]
                new_y = cube["E"][1][1] - rel_y - 1
                move = 0
            case "C":
                new_x = cube["E"][0][0] + rel_y
                new_y = cube["E"][1][0]
                move = 1
            case "E":
                new_x = cube["B"][0][0]
                new_y = cube["B"][1][1] - rel_y - 1
                move = 0
            case "F":
                new_x = cube["B"][0][0] + rel_y
                new_y = cube["B"][1][0]
                move = 1
    elif new_x >= max_x:
        match face:
            case "A":
                new_x = cube["D"][0][1] - 1
                new_y = cube["D"][1][1] - rel_y - 1
                move = 2
            case "C":
                new_x = cube["A"][0][0] + rel_y
                new_y = cube["A"][1][1] - 1
                move = 3
            case "D":
                new_x = cube["A"][0][1] - 1
                new_y = cube["A"][1][1] - rel_y - 1
                move = 2
            case "F":
                new_x = cube["D"][0][0] + rel_y
                new_y = cube["D"][1][1] - 1
                move = 3
    elif new_y < min_y:
        match face:
            case "A":
                new_x = cube["F"][0][0] + rel_x
                new_y = cube["F"][1][1] - 1
                move = 3
            case "B":
                new_x = cube["F"][0][0]
                new_y = cube["F"][1][0] + rel_x
                move = 0
            case "E":
                new_x = cube["C"][0][0]
                new_y = cube["C"][1][0] + rel_x
                move = 0
    elif new_y >= min_y:
        match face:
            case "A":
                new_x = cube["C"][0][1] - 1
                new_y = cube["C"][1][0] + rel_x
                move = 2
            case "D":
                new_x = cube["F"][0][1] - 1
                new_y = cube["F"][1][0] + rel_x
                move = 2
            case "F":
                new_x = cube["A"][0][0] + rel_x
                new_y = cube["A"][1][0]
                move = 1

    return new_x, new_y, move


def solution_day22_prob2(puzzle_in: list):
    # Parse the board and the commands
    board = puzzle_in[:-2]
    path = puzzle_in.pop(-1)
    commands = path.replace("R", " R ").replace("L", " L ").split(" ")

    # Find start and end for each row
    max_col = 0
    for row in board:
        valid = re.search(r"[.#]+", row)
        max_col = max(max_col, valid.end())

    # Board sorted by columns
    col_board = [[] for _ in range(max_col)]
    for row in board:
        for index, item in enumerate(row):
            col_board[index] += [item]

    # Start position
    pos = [board[0].index("."), 0]

    drawn_board = board.copy()
    drawn_board = list(map(list, drawn_board))

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

                # print(new_x, new_y, move)
                new_x, new_y, new_move = step(new_x, new_y, move)
                # print(new_x, new_y, move, "\n")
                # input("\n")

                # See if we collide with a wall
                if board[new_y][new_x] == "#":
                    break
                else:
                    pos = [new_x, new_y]
                    move = new_move

                drawn_board[pos[1]][pos[0]] = ">" if move == 0 else "v" if move == 1 else "<" if move == 2 else "^"
            drawn_board[pos[1]][pos[0]] = ">" if move == 0 else "v" if move == 1 else "<" if move == 2 else "^"
        drawn_board[pos[1]][pos[0]] = ">" if move == 0 else "v" if move == 1 else "<" if move == 2 else "^"
    for row in drawn_board:
        print("".join(row))
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + move


# Tests and Solution ---
# print("Tests:")
# print(solution_day22_prob2(test01))
print("\nSolution:")
print(solution_day22_prob2(puzzle))

# 128006 is too high
