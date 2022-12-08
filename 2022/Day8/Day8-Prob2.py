# Solution for Problem 2 Day 8 of AoC 2022!

# Puzzle Input ----------
with open('Day8-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day8-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Calculate scenis score
def scenic_score(views: tuple) -> int:
    total = 1
    for item in views:
        total *= item
    return total


# Get the view from a specific tree
def check_view(x: int, y: int, h: int, x_max: int, y_max: int, trees: list) -> tuple:
    view = [0, 0, 0, 0]
    for x_check in range(x - 1, -1, -1):
        view[0] += 1
        if trees[y][x_check] >= h:
            break

    for x_check in range(x + 1, x_max):
        view[1] += 1
        if trees[y][x_check] >= h:
            break

    for y_check in range(y - 1, -1, -1):
        view[2] += 1
        if trees[y_check][x] >= h:
            break

    for y_check in range(y + 1, y_max):
        view[3] += 1
        if trees[y_check][x] >= h:
            break

    return tuple(view)


def solution_day8_prob2(puzzle_in: list):
    # Parse the input
    trees = list(map(list, puzzle_in))
    for index, item in enumerate(trees):
        trees[index] = list(map(int, item))
    x_max, y_max = len(trees[0]), len(trees)

    # Get the columns
    cols = [[] for _ in range(x_max)]
    for y, row in enumerate(trees):
        for x, tree in enumerate(row):
            cols[x] += [tree]

    # Calculate maximum score
    scores = []
    for y, row in enumerate(trees):
        for x, tree in enumerate(row):
            view = check_view(x, y, tree, x_max, y_max, trees)
            scores += [scenic_score(view)]

    return max(scores)


# Tests and Solution ---
print("Tests:")
print(solution_day8_prob2(test01))
print("\nSolution:")
print(solution_day8_prob2(puzzle))
