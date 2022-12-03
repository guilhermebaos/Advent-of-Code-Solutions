# Solution for Problem 1 Day 2 of AoC 2022!

# Puzzle Input ----------
with open('Day2-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day2-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------

# Score of a round of Rock Paper Scissors
def game_score(opp: str, pla: str) -> int:
    opp = (ord(opp) - ord("A"))
    pla = (ord(pla) - ord("X"))

    return (pla + 1) + (3 if pla == opp else 6 if (pla - 1) % 3 == opp else 0)


def solution_day2_prob1(puzzle_in: list) -> int:
    total = 0

    # Get the plays of each round and calculate the total score
    for item in puzzle_in:
        o, p = item.split(" ")
        total += game_score(o, p)
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day2_prob1(test01))
print("\nSolution:")
print(solution_day2_prob1(puzzle))

# 14000 is too high
# 11135 is too low
