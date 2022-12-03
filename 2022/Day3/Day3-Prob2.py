# Solution for Problem 2 Day 3 of AoC 2022!

# Puzzle Input ----------
with open('Day3-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day3-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day3_prob2(puzzle_in: list):
    total = 0
    for index in range(len(puzzle_in) // 3):
        a, b, c = set(puzzle_in[3 * index]), set(puzzle_in[3 * index + 1]), set(puzzle_in[3 * index + 2])
        char_num = ord(list(a.intersection(b).intersection(c))[0])
        total += 1 + char_num + (-ord("a") if ord("a") <= char_num <= ord("z") else -ord("A") + 26)
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day3_prob2(test01))
print("\nSolution:")
print(solution_day3_prob2(puzzle))
