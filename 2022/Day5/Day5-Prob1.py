# Solution for Problem 1 Day 5 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day5-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day5-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Parse the crates into lists
def parse_crate(drawing: list) -> list:
    columns = int(drawing[-1][-1])
    crates = [[] for x in range(columns)]

    # Get the crates from top to bottom
    for item in drawing[::-1][1:]:
        for i in range(columns):

            # Add a crate to a list
            try:
                box = item[4 * i + 1]
                if box != ' ':
                    crates[i] += [box]
            except IndexError:
                continue

    return crates


# Execute a move
def do_move(crates: list, move: str) -> list:
    # Parse the move order
    num, from_col, to_col = list(map(int, list(re.split("move\s|\sfrom\s|\sto\s", move))[1:]))

    # Get the crates in reverse order and add them to the right stack
    moving = crates[from_col - 1][-num:]
    crates[from_col - 1] = crates[from_col - 1][:-num]
    crates[to_col - 1] += moving[::-1]
    return crates


def solution_day5_prob1(puzzle_in: list):
    # Separate the drawing from the orders
    space = puzzle_in.index('')
    drawing = puzzle_in[:space]
    moves = puzzle_in[space + 1:]

    # Execute the orders
    crates = parse_crate(drawing)
    for m in moves:
        crates = do_move(crates, m)

    # Return the message
    message = ''.join([stack[-1] for stack in crates])

    return message


# Tests and Solution ---
print("Tests:")
print(solution_day5_prob1(test01))
print("\nSolution:")
print(solution_day5_prob1(puzzle))
