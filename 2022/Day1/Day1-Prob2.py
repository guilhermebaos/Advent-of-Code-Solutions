# Solution for Problem 2 Day 1 of AoC 2022!

# Puzzle Input ----------
with open('Day1-Input.txt', 'r') as file:
    puzzle = file.read().split("\n\n")

with open('Day1-Test01.txt', 'r') as file:
    test01 = file.read().split("\n\n")


# Code ------------------
def solution_day1_prob2(puzzle_in: list):
    calories = []
    for item in puzzle_in:
        calories += [sum(map(int, item.split("\n")))]

    calories.sort(reverse=True)

    return calories[0] + calories[1] + calories[2]


# Tests and Solution ---
print("Tests:")
print(solution_day1_prob2(test01))
print("\nSolution:")
print(solution_day1_prob2(puzzle))
