# Solution for Problem 1 Day 13 of AoC 2022!
import string

# Puzzle Input ----------
with open('Day13-Input.txt', 'r') as file:
    puzzle = file.read().split("\n\n")

with open('Day13-Test01.txt', 'r') as file:
    test01 = file.read().split("\n\n")


# Code ------------------

# Parse packages into python lists
def parse_package(package: str, index: int) -> (list, int):
    parsed = []
    while index < len(package):
        item = package[index]

        # Parse the sublist
        if item == "[":
            sub_parsed = parse_package(package, index + 1)
            parsed += [sub_parsed[0]]
            index = sub_parsed[1]

        # End this parsing
        elif item == "]":
            return parsed, index

        # Add an integer
        elif item in string.digits:
            number = ""
            while item in string.digits:
                number += item
                index += 1
                item = package[index]
            index -= 1
            parsed += [int(number)]
        index += 1
    return [], 0


# Checks if p1 < p2
def compare_packages(p1: list, p2: list) -> bool | None:
    for item1, item2 in zip(p1, p2):

        # Compare integers
        if type(item1) == type(item2) == int:
            if item1 == item2:
                continue
            return item1 < item2

        # Compare lists
        elif type(item1) == type(item2) == list:
            value = compare_packages(item1, item2)
            if value is None:
                continue
            return value

        # Compare an integer and a list
        else:
            if type(item1) == int:
                item1 = [item1]
            if type(item2) == int:
                item2 = [item2]

            value = compare_packages(item1, item2)
            if value is None:
                continue
            return value

    # Compare list lengths
    lp1, lp2 = len(p1), len(p2)
    if lp1 == lp2:
        return None
    return lp1 < lp2


def solution_day13_prob1(puzzle_in: list):
    pairs = list(map(lambda x: x.split("\n"), puzzle_in))

    # Parse the packages
    parsed = []
    for p in pairs:
        parsed += [[parse_package(p[0], 1)[0], parse_package(p[1], 1)[0]]]

    # Get the total indices of ordered pairs
    total = 0
    for index, pair in enumerate(parsed):
        truth = compare_packages(pair[0], pair[1])
        total += truth * (index + 1)

    return total


# Tests and Solution ---
print("Tests:")
print(solution_day13_prob1(test01))
print("\nSolution:")
print(solution_day13_prob1(puzzle))
