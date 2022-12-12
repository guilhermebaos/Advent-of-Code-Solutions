# Solution for Problem 1 Day 12 of AoC 2022!

# Puzzle Input ----------
with open('Day12-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day12-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Get squares adjacent to this one
def explore(current: (int, int), maze: list[list[int]], max_x: int, max_y: int) -> set:
    # Current coordinates
    x, y = current
    h = maze[y][x]

    # Analise nearby squares and see if their height is lower than current height
    possible = set()
    for delta in [-1, 1]:
        new_x = x + delta
        new_y = y + delta
        if new_x < 0 or new_x >= max_x:
            pass
        else:
            new_h = maze[y][new_x]
            if new_h <= h+1:
                possible.add((new_x, y))

        if new_y < 0 or new_y >= max_y:
            pass
        else:
            new_h = maze[new_y][x]
            if new_h <= h + 1:
                possible.add((x, new_y))

    return possible


def solution_day12_prob1(puzzle_in: list):
    # Parse the maze
    maze = [[ord(h) for h in item] for item in puzzle_in]
    max_y, max_x = len(maze), len(maze[0])

    # Get the starting and ending squares
    start, end = [], []
    for y, row in enumerate(maze):
        for x, h in enumerate(row):
            if h == ord("S"):
                start = (x, y)
                maze[y][x] = ord("a")
            elif h == ord("E"):
                end = (x, y)
                maze[y][x] = ord("z")

    # Explore the maze
    visited = set()
    paths = [[start]]
    while True:
        # Get current path
        item = paths.pop(0)
        current = item[-1]
        possible = explore(current, maze, max_x, max_y)

        # Explore next possibilities
        for next_up in possible:
            if next_up in visited:
                continue

            visited.add(next_up)
            paths += [item + [next_up]]
            if next_up == end:
                return len(item)


# Tests and Solution ---
print("Tests:")
print(solution_day12_prob1(test01))
print("\nSolution:")
print(solution_day12_prob1(puzzle))
