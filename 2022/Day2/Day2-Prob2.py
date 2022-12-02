# Solution for Problem 2 Day 2 of AoC 2022!

# Puzzle Input ----------
with open('Day2-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day2-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def game_score(opp: str, pla: str) -> int:
    opp = (ord(opp) - ord("A"))

    pla = (opp - 1 if pla == "X" else opp if pla == "Y" else opp + 1) % 3

    return (pla + 1) + (3 if pla == opp else 6 if (pla - 1) % 3 == opp else 0)


def solution_day2_prob2(puzzle_in: list) -> int:
    total = 0
    for item in puzzle_in:
        o, p = item.split(" ")
        total += game_score(o, p)
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day2_prob2(test01))
print("\nSolution:")
print(solution_day2_prob2(puzzle))
