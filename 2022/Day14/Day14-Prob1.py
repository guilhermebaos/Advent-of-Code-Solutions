# Solution for Problem 1 Day 14 of AoC 2022!

# Puzzle Input ----------
with open('Day14-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day14-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def wall(p1: (int, int), p2: (int, int)) -> set[tuple]:
    # Vertical Wall
    if p1[0] == p2[0]:
        x = p1[0]
        y_start, y_end = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])
        new_wall = set((x, y) for y in range(y_start, y_end + 1))

    # Horizontal Wall
    else:
        y = p1[1]
        x_start, x_end = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
        new_wall = set((x, y) for x in range(x_start, x_end + 1))

    return new_wall


def move_sand(position: list[int], occupied: set[tuple]) -> list[int] | bool:
    # Possible moves
    down = [position[0], position[1] + 1]
    down_left = [position[0] - 1, position[1] + 1]
    down_right = [position[0] + 1, position[1] + 1]

    # Try to move the grain of sand
    if tuple(down) not in occupied:
        return down
    elif tuple(down_left) not in occupied:
        return down_left
    elif tuple(down_right) not in occupied:
        return down_right

    return False


# Add a new sand
def sand(max_y: int, occupied: set[tuple]) -> tuple[int] | bool:
    position = [500, 0]

    while True:
        # Try to move the sand
        new_position = move_sand(position, occupied)
        if not new_position:
            break

        # Sand falls in the void
        if new_position[1] >= max_y:
            return False

        position = new_position[:]

    return tuple(position)


def solution_day14_prob1(puzzle_in: list):
    # Parse the input
    parsed = list(map(lambda x: list(map(lambda y: list(map(int, y.split(","))), x.split(" -> "))), puzzle_in))
    occupied = set()

    # Create the walls
    max_y = 0
    for line in parsed:
        for index in range(len(line) - 1):
            max_y = max(max_y, line[index][1])
            occupied.update(wall(line[index], line[index + 1]))

    new_sand = True
    total = 0
    while new_sand:
        # Try to add a new sand
        new_sand = sand(max_y, occupied)
        if not new_sand:
            break

        # Mark the sand as an occupied spot
        occupied.update({new_sand})
        total += 1

    return total


# Tests and Solution ---
print("Tests:")
print(solution_day14_prob1(test01))
print("\nSolution:")
print(solution_day14_prob1(puzzle))
