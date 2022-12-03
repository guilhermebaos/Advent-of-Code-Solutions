# Solution for Problem 1 Day 3 of AoC 2022!

# Puzzle Input ----------
with open('Day3-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day3-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day3_prob1(puzzle_in: list):
    total = 0
    for item in puzzle_in:

        # Separate both compartments
        len_item = len(item)
        a, b = set(item[0:len_item // 2]), set(item[len_item // 2:])

        # Get the common character and get its priority
        char_num = ord(list(a.intersection(b))[0])
        total += 1 + char_num + (-ord("a") if ord("a") <= char_num <= ord("z") else -ord("A") + 26)
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day3_prob1(test01))
print("\nSolution:")
print(solution_day3_prob1(puzzle))
