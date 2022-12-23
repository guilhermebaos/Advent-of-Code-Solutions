# Solution for Problem 2 Day 23 of AoC 2022!

# Puzzle Input ----------
with open('Day23-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day23-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Deltas for E, SE, S, SW, W, NW, N, NE
deltas = {
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
    "N": (0, -1),
    "NE": (1, -1)
}
directions = list(deltas.keys())


# Move all elves, supposing no more than two elves would propose going to the same spot
def move(elves: list, order: list[str]) -> list:
    new_elves = []
    for num, elf in enumerate(elves):
        # Adjacent spaces
        adjacent = {d: [elf[0] + deltas[d][0], elf[1] + deltas[d][1]] for d in deltas}

        # Blocked adjacent spaces
        blocked = set()
        for d in adjacent:
            if adjacent[d] in elves:
                blocked.add(d)

        # If no spaces are blocked, don't move
        if len(blocked) == 0:
            new_elves += [elf]
        else:
            # Try to move in the order given
            for direc in order:
                if direc == "N" and len({"N", "NE", "NW"}.intersection(blocked)) == 0:
                    d = deltas[direc]
                    break
                elif direc == "S" and len({"S", "SE", "SW"}.intersection(blocked)) == 0:
                    d = deltas[direc]
                    break
                elif direc == "W" and len({"W", "SW", "NW"}.intersection(blocked)) == 0:
                    d = deltas[direc]
                    break
                elif direc == "E" and len({"E", "SE", "NE"}.intersection(blocked)) == 0:
                    d = deltas[direc]
                    break
            else:
                d = (0, 0)

            # See if this position is already occupied, if it is don't move
            new_pos = [elf[0] + d[0], elf[1] + d[1]]
            try:
                conflict = new_elves.index(new_pos)
                new_elves[conflict] = elves[conflict].copy()
                new_elves += [elf]
            except ValueError:
                new_elves += [new_pos]
    return new_elves


def solution_day23_prob2(puzzle_in: list):
    elves = []
    for y, row in enumerate(puzzle_in):
        for x, item in enumerate(row):
            if item == "#":
                elves += [[x, y]]

    num_elves = len(elves)
    order = ["N", "S", "W", "E"]
    rounds = 0
    while True:
        # Gather the elves' new positions
        new_elves = move(elves, order)
        rounds += 1
        if new_elves == elves:
            break
        else:
            elves = new_elves.copy()
        order += [order.pop(0)]
        if rounds % 10 == 0:
            print(rounds)
    return rounds


# Tests and Solution ---
print("Tests:")
print(solution_day23_prob2(test01))
print("\nSolution:")
print(solution_day23_prob2(puzzle))
