# Solution for Problem 2 Day 24 of AoC 2022!
from math import lcm

# Puzzle Input ----------
with open('Day24-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day24-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------

# Movment of the blizzards/ expedition
moves = {
    "right": (1, 0),
    "left": (-1, 0),
    "down": (0, 1),
    "up": (0, -1),
    "wait": (0, 0)
}


def go(start: (int, int), end: (int, int), t0: int, blizzards: list[set], period: int, max_x: int, max_y: int) -> int:
    # Each item to explore is (x, y, t)
    to_explore = [(start[0], start[1], t0)]
    visited = dict()

    # Max times we can visit each spot
    cutoff = 10

    while True:
        # Current blizards and positions
        cur_x, cur_y, cur_t = to_explore.pop(0)

        # Next blizzards and total obstacles/ visited spaces
        new_t = cur_t + 1
        obstacles = blizzards[new_t % period]

        # Check if we visited this spot in this exact time or at least cutoff times
        cur_visited = visited.get((cur_x, cur_y), set())
        if new_t in cur_visited or len(cur_visited) > cutoff:
            continue

        for m in moves:
            new_x = cur_x + moves[m][0]
            new_y = cur_y + moves[m][1]

            # Reached the end
            if (new_x, new_y) == end:
                return new_t

            if (new_x, new_y) == start and new_t < t0 + cutoff:
                pass

            # Check if the spot is off bounds
            elif new_x <= 0 or new_x >= max_x - 1 or new_y <= 0 or new_y >= max_y - 1:
                continue

            # Check for obstacles
            if (new_x, new_y) not in obstacles and (new_x, new_y, new_t) not in to_explore:
                to_explore += [(new_x, new_y, new_t)]

        visited[(cur_x, cur_y)] = visited.get((cur_x, cur_y), set()).union({cur_t})


def solution_day24_prob2(puzzle_in: list):
    memory = []

    valley = list(map(list, puzzle_in))
    start = (valley[0].index("."), 0)
    end = (valley[-1].index("."), len(valley) - 1)
    max_x, max_y = len(valley[0]), len(valley)

    # Get position of all blizzards in t = 0 and all wall positions
    blizzards = {
        "right": set(),
        "left": set(),
        "up": set(),
        "down": set()
    }
    for y, row in enumerate(valley):
        for x, item in enumerate(row):
            if item == ">":
                blizzards["right"].add((x, y))
            elif item == "<":
                blizzards["left"].add((x, y))
            elif item == "^":
                blizzards["up"].add((x, y))
            elif item == "v":
                blizzards["down"].add((x, y))

    memory += [blizzards]

    # Calculate all possible blizzards
    period = lcm(max_x - 2, max_y - 2)
    for _ in range(0, period):
        blizzards = memory[-1]
        new_blizzards = dict()
        for direction in blizzards:
            new_blizzards[direction] = set()
            m = moves[direction]
            for item in blizzards[direction]:
                x, y = item
                new_blizzards[direction].add((
                    (x + m[0] - 1) % (max_x - 2) + 1,
                    (y + m[1] - 1) % (max_y - 2) + 1
                ))
        memory += [new_blizzards]

    # Get the blizzardsp positions, we don't need their direction anymore
    blizzards = []
    for new_bliz in memory:
        obstacles = set()
        for direction in new_bliz:
            for b in new_bliz[direction]:
                obstacles.add((b[0], b[1]))
        blizzards += [obstacles]

    t1 = go(start, end, 0, blizzards, period, max_x, max_y)
    t2 = go(end, start, t1, blizzards, period, max_x, max_y)
    t3 = go(start, end, t2, blizzards, period, max_x, max_y)
    return t3


# Tests and Solution ---
print("Tests:")
print(solution_day24_prob2(test01))
print("\nSolution:")
print(solution_day24_prob2(puzzle))
