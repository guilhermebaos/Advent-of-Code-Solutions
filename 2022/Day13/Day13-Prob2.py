# Solution for Problem 2 Day 13 of AoC 2022!
from functools import cmp_to_key

# Puzzle Input ----------
with open('Day13-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day13-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

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


def solution_day13_prob2(puzzle_in: list):
    # Get all packages
    packages = list(filter(lambda x: x != "", puzzle_in))
    packages = list(map(eval, packages))

    # Insert sort the packages
    sorted_pairs = [packages.pop()]
    for new_item in packages:
        for index, old_item in enumerate(sorted_pairs):
            if compare_packages(new_item, old_item):
                sorted_pairs.insert(index, new_item)
                break
        else:
            sorted_pairs += [new_item]

    # Multiply the indexes of the divider packats
    return (sorted_pairs.index([[2]]) + 1) * (sorted_pairs.index([[6]]) + 1)


# Tests and Solution ---
print("Tests:")
print(solution_day13_prob2(test01))
print("\nSolution:")
print(solution_day13_prob2(puzzle))
