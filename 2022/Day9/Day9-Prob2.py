# Solution for Problem 2 Day 9 of AoC 2022!

# Puzzle Input ----------
with open('Day9-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day9-Test02.txt', 'r') as file:
    test02 = file.read().split("\n")

# Code ------------------
pos_knots = [[0, 0] for _ in range(10)]
visited = set()


# Calculate chess distance between two points
def chess_distance(pos1: [int, int], pos2: [int, int]) -> int:
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))


# Execute a one-step move in a given direction
def do_move(direction: str, index_h: int):
    global pos_knots, visited
    pos_h = pos_knots[index_h]

    if direction == "R":
        pos_h[0] += 1
    elif direction == "L":
        pos_h[0] -= 1
    elif direction == "D":
        pos_h[1] -= 1
    elif direction == "U":
        pos_h[1] += 1

    pos_knots[index_h] = pos_h
    return


# Check the distance between two knots, and move them if necessary
def check_distance(index_h: int, index_t: int):
    global pos_knots
    pos_h, pos_t = pos_knots[index_h], pos_knots[index_t]

    if chess_distance(pos_h, pos_t) > 1:
        for i in [0, 1]:
            pos_t[i] += 0 if pos_t[i] == pos_h[i] else -((pos_t[i] > pos_h[i]) * 2 - 1)

    pos_knots[index_h], pos_knots[index_t] = pos_h, pos_t
    return


def solution_day9_prob2(puzzle_in: list):
    # Set global variables
    global pos_knots, visited

    pos_knots = [[0, 0] for _ in range(10)]
    visited = set()

    # Parse the moves
    moves = []
    for item in puzzle_in:
        moves += [item.split(' ')]

    # Execute the moves
    for m in moves:
        for num in range(int(m[1])):
            do_move(m[0], 0)
            for i in range(9):
                check_distance(i, i+1)
            visited.add(tuple(pos_knots[9]))

    # Calculate the number of places visited
    return len(visited)


# Tests and Solution ---
print("Tests:")
print(solution_day9_prob2(test02))
print("\nSolution:")
print(solution_day9_prob2(puzzle))
