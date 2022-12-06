# Solution for Problem 1 Day 6 of AoC 2022!

# Puzzle Input ----------
with open('Day6-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day6-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day6_prob1(puzzle_in: list):
    char_list = []

    # Process each line
    for item in puzzle_in:
        char_num = 0
        for i in range(len(item) - 3):

            # See if four sequential characters are different
            if len(set(item[i:i+4])) == 4:
                char_num = i + 4
                break
        char_list += [char_num]
    return char_list


# Tests and Solution ---
print("Tests:")
print(solution_day6_prob1(test01))
print("\nSolution:")
print(solution_day6_prob1(puzzle))
