# Solution for Problem 1 Day 9 of AoC 2022!

# Puzzle Input ----------
with open('Day9-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day9-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
pos_h, pos_t = [0, 0], [0, 0]
visited = set()


# Calculate chess distance between two points
def chess_distance() -> int:
    global pos_h, pos_t, visited

    return max(abs(pos_h[0] - pos_t[0]), abs(pos_h[1] - pos_t[1]))


# Execute a one-step move in a given direction
def do_move(direction: str):
    global pos_h, pos_t, visited

    if direction == "R":
        pos_h[0] += 1
    elif direction == "L":
        pos_h[0] -= 1
    elif direction == "D":
        pos_h[1] -= 1
    elif direction == "U":
        pos_h[1] += 1

    if chess_distance() > 1:
        for i in [0, 1]:
            pos_t[i] += 0 if pos_t[i] == pos_h[i] else -((pos_t[i] > pos_h[i]) * 2 - 1)
    visited.add(tuple(pos_t))

    return


def solution_day9_prob1(puzzle_in: list):
    # Set global variables
    global pos_h, pos_t, visited

    pos_h, pos_t = [0, 0], [0, 0]
    visited = set()

    # Parse the moves
    moves = []
    for item in puzzle_in:
        moves += [item.split(' ')]

    # Execute the moves
    for m in moves:
        for num in range(int(m[1])):
            do_move(m[0])

    # Calculate the number of places visited
    return len(visited)


# Tests and Solution ---
print("Tests:")
print(solution_day9_prob1(test01))
print("\nSolution:")
print(solution_day9_prob1(puzzle))

# 6036 is too high
