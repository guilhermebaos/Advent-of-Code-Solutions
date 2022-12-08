# Solution for Problem 1 Day 8 of AoC 2022!

# Puzzle Input ----------
with open('Day8-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day8-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Check the visibility within a line
def check_visibility(x: int, y: int, mode: str, line: list, visible: list) -> list:
    for i in range(2):

        # Reverse direction
        if i == 1:
            line = line[::-1]

        # Get visibility
        max_height = -1
        for z, tree in enumerate(line):

            # If we can see the tree...
            if tree > max_height:

                # ... add it to total
                max_height = tree

                # ... and mark it as visible on the right row or column
                if mode == "row":
                    visible[y][z if i == 0 else -(z+1)] = True
                elif mode == "col":
                    visible[z if i == 0 else -(z+1)][x] = True

    return visible


def solution_day8_prob1(puzzle_in: list):
    # Parse the input
    trees = list(map(list, puzzle_in))
    for index, item in enumerate(trees):
        trees[index] = list(map(int, item))
    x_max, y_max = len(trees[0]), len(trees)

    # Visible trees
    visible = [[0 for _ in range(x_max)] for _ in range(y_max)]

    # Get the columns and check visibility
    cols = [[] for _ in range(x_max)]
    for y, row in enumerate(trees):
        visible = check_visibility(0, y, "row", row, visible)
        for x, tree in enumerate(row):
            cols[x] += [tree]
    for x, col in enumerate(cols):
        visible = check_visibility(x, 0, "col", col, visible)

    # Total number of visible trees
    total = 0
    for row in visible:
        for item in row:
            total += item

    return total


# Tests and Solution ---
print("Tests:")
print(solution_day8_prob1(test01))
print("\nSolution:")
print(solution_day8_prob1(puzzle))
