# Solution for Problem 2 Day 4 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day4-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day4-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day4_prob2(puzzle_in: list):
    total = 0
    for item in puzzle_in:
        # Get range values
        start1, end1, start2, end2 = list(map(int, re.split("[,-]", item)))

        # See if there is overlapping
        if start2 <= end1 <= end2:
            total += 1
        elif start1 <= end2 <= end1:
            total += 1
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day4_prob2(test01))
print("\nSolution:")
print(solution_day4_prob2(puzzle))
