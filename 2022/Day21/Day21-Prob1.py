# Solution for Problem 1 Day 21 of AoC 2022!

# Puzzle Input ----------
with open('Day21-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day21-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day21_prob1(puzzle_in: list):
    monkeys = list(map(lambda x: x.replace(":", "").split(" "), puzzle_in))
    monkeys = {x[0]: int(x[1]) if len(x[1:]) == 1 else x[1:] for x in monkeys}

    # Run the monkey's operations until we have root's number
    while not isinstance(monkeys["root"], int):
        for name in monkeys:
            value = monkeys[name]
            if isinstance(value, int):
                continue

            # Execute the other monkey's operations
            m1, op, m2 = value
            if isinstance(monkeys[m1], int) and isinstance(monkeys[m2], int):
                monkeys[name] = eval(f"{monkeys[m1]} {op if op != '/' else '//'} {monkeys[m2]}")

    return monkeys["root"]


# Tests and Solution ---
print("Tests:")
print(solution_day21_prob1(test01))
print("\nSolution:")
print(solution_day21_prob1(puzzle))
