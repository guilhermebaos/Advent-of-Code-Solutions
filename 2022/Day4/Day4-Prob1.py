# Solution for Problem 1 Day 4 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day4-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day4-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day4_prob1(puzzle_in: list):
    total = 0
    for item in puzzle_in:
        # Get range values
        start1, end1, start2, end2 = list(map(int, re.split("[,-]", item)))

        # See if 1 is inside 2
        if start2 <= start1 and end1 <= end2:
            total += 1

        # See if 2 is inside 1
        elif start1 <= start2 and end2 <= end1:
            total += 1
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day4_prob1(test01))
print("\nSolution:")
print(solution_day4_prob1(puzzle))

# 522 is too high
