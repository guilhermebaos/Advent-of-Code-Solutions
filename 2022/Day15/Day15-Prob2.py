# Solution for Problem 2 Day 15 of AoC 2022!

# Puzzle Input ----------
with open('Day15-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day15-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Calculate the Manhattan distance between two points
def man_distance(p1: (int, int), p2: (int, int)) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Union of two integer intervals
def union_intervals(p1: (int, int), p2: (int, int)) -> tuple | None:
    if p1[0] < p2[0]:
        if p1[1] < p2[0]:
            return None
        else:
            return p1[0], max(p1[1], p2[1])
    elif p2[0] < p1[0]:
        if p2[1] < p1[0]:
            return None
        else:
            return p2[0], max(p1[1], p2[1])
    else:
        return p1[0], max(p1[1], p2[1])


# Intersection of integer intervals
def intersection_intervals(p1: (int, int), p2: (int, int)) -> tuple | None:
    mini = max(p1[0], p2[0])
    maxi = min(p1[1], p2[1])

    if mini > maxi:
        return None
    else:
        return mini, maxi


# Find a free space in the middle of occupied intervals
def free(x_min: int, x_max: int, occupied: list[tuple[int]]) -> int:
    # Focus on the interesting zone
    occupied = list(map(lambda x: intersection_intervals((x_min, x_max), x), occupied))
    occupied = list(filter(lambda x: x is not None, occupied))

    # Union of all intervals
    while len(occupied) > 2:
        item = occupied.pop(0)
        for i in range(len(occupied)):
            other = occupied.pop(0)
            union = union_intervals(item, other)
            if union:
                occupied += [union]
                break
            else:
                occupied += [other]
        else:
            occupied += [item]

    if len(occupied) == 1:
        return -1
    p1, p2 = occupied[0], occupied[1]
    if union_intervals(p1, p2):
        return -1
    else:
        if p1[1] < p2[0]:
            return p1[1] + 1
        else:
            return p2[1] + 1


def solution_day15_prob2(puzzle_in: list):
    limit_x, limit_y = 4000000, 4000000

    # Parse inputs
    puzzle_in = list(map(lambda x: (x.replace(",", "").replace(":", "")).split(" "), puzzle_in))
    sensors = dict()
    for item in puzzle_in:
        sx, sy = int(item[2].split("=")[1]), int(item[3].split("=")[1])
        bx, by = int(item[-2].split("=")[1]), int(item[-1].split("=")[1])

        sensors[(sx, sy)] = (bx, by)

    # Get distances from beacons to sensors
    distances = dict()
    beacons = set()
    for item in sensors:
        beacon = sensors[item]
        beacons.add(beacon)
        distances[item] = man_distance(item, beacon)

    for row in range(limit_y + 1):
        # Occupied intervals in the selected row
        occupied = []
        for item in distances:
            d = distances[item]
            v_dist = abs(item[1] - row)
            h_dist = d - v_dist

            if h_dist >= 0:
                occupied += [(item[0] - h_dist, item[0] + h_dist)]

        # Find the free spot and return its value
        free_x = free(0, limit_x, occupied)
        if row % 100000 == 0:
            print(row)
        if free_x != -1:
            return 4000000 * free_x + row
    return -1


# Tests and Solution ---
print("Tests:")
print(solution_day15_prob2(test01))
print("\nSolution:")
print(solution_day15_prob2(puzzle))
