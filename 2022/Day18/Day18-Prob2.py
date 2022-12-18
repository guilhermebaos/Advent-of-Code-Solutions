# Solution for Problem 2 Day 18 of AoC 2022!

# Puzzle Input ----------
with open('Day18-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day18-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Find all points nearby of current point
def nearby(current: (int, int, int), air: list[tuple[int]]) -> list[tuple]:
    neighboors = []
    for delta in [-1, 1]:
        neighboors += [(current[0] + delta, current[1], current[2])]
        neighboors += [(current[0], current[1] + delta, current[2])]
        neighboors += [(current[0], current[1], current[2] + delta)]

    neighboors = list(filter(lambda x: x in air, neighboors))
    return neighboors


# Find all air points that can escape to the outside of tha lava drop
def air_escape(start: (int, int, int), air: list[tuple[int]]) -> set:
    explore = [start]
    visited = set()
    while len(explore) > 0:
        current_air = explore.pop(0)
        for next_air in nearby(current_air, air):
            if next_air in visited:
                continue
            else:
                visited.add(next_air)
                explore += [next_air]
    return visited


# Calculate the surface area
def surface_area(coords: list[tuple[int]]) -> int:
    total = 0
    for item in coords:
        total += 6
        for delta in [-1, 1]:
            total -= (item[0] + delta, item[1], item[2]) in coords
            total -= (item[0], item[1] + delta, item[2]) in coords
            total -= (item[0], item[1], item[2] + delta) in coords

    return total


def solution_day18_prob2(puzzle_in: list):
    lava = list(map(lambda c: tuple(map(int, c.split(","))), puzzle_in))
    limits = [[0, 0] for _ in range(3)]

    # Find total surface area
    for item in lava:
        for index in range(3):
            limits[index][0] = min(limits[index][0], item[index])
            limits[index][1] = max(limits[index][1], item[index])

    # Extend limits
    for index in range(3):
        limits[index][0] -= 1
        limits[index][1] += 1

    # Air in the grid
    air = []
    for x in range(limits[0][0], limits[0][1]):
        for y in range(limits[1][0], limits[1][1]):
            for z in range(limits[2][0], limits[2][1]):
                item = (x, y, z)
                if item in lava:
                    continue
                air += [item]

    # Air reachable from outside
    not_trapped = air_escape((-1, -1, -1), air)
    trapped = list(set(air.copy()).difference(not_trapped))
    return surface_area(lava) - surface_area(trapped)


# Tests and Solution ---
print("Tests:")
print(solution_day18_prob2(test01))
print("\nSolution:")
print(solution_day18_prob2(puzzle))
