# Solution for Problem 1 Day 18 of AoC 2022!

# Puzzle Input ----------
with open('Day18-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day18-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day18_prob1(puzzle_in: list):
    coords = list(map(lambda x: tuple(map(int, x.split(","))), puzzle_in))
    total = 0

    # Find total surface area
    for item in coords:
        total += 6
        for delta in [-1, 1]:
            total -= (item[0] + delta, item[1], item[2]) in coords
            total -= (item[0], item[1] + delta, item[2]) in coords
            total -= (item[0], item[1], item[2] + delta) in coords
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day18_prob1(test01))
print("\nSolution:")
print(solution_day18_prob1(puzzle))
