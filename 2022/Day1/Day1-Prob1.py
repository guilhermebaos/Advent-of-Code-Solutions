# Solution for Problem 1 Day 1 of AoC 2022!

# Puzzle Input ----------
with open('Day1-Input.txt', 'r') as file:
    puzzle = file.read().split("\n\n")

with open('Day1-Test01.txt', 'r') as file:
    test01 = file.read().split("\n\n")


# Code ------------------
def solution_day1_prob1(puzzle_in: list):
    maxi = 0
    for item in puzzle_in:
        maxi = max(maxi, sum(map(int, item.split("\n"))))

    return maxi


# Tests and Solution ---
print("Tests:")
print(solution_day1_prob1(test01))
print("\nSolution:")
print(solution_day1_prob1(puzzle))
