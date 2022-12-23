# Solution for Problem 2 Day 21 of AoC 2022!

# Puzzle Input ----------
with open('Day21-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day21-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day21_prob2(puzzle_in: list):
    monkeys = list(map(lambda x: x.replace(":", "").split(" "), puzzle_in))
    monkeys = {x[0]: int(x[1]) if len(x[1:]) == 1 else x[1:] for x in monkeys}
    monkeys["root"][1] = "=="
    monkeys["humn"] = "X"

    # Calculate all numbers that can be calculated without using X
    complexity = {"+", "-", "*", "/", "X"}
    while not isinstance(monkeys[monkeys["root"][2]], int):
        for name in monkeys:
            value = monkeys[name]
            if isinstance(value, int) or value == "X":
                continue

            # Execute the other monkey's operations
            m1, op, m2 = value
            if isinstance(monkeys[m1], int) and isinstance(monkeys[m2], int):
                monkeys[name] = eval(f"{monkeys[m1]} {op if op != '/' else '//'} {monkeys[m2]}")

    # Run all remaining operations backward to make sure the equality holds
    current = [monkeys["root"][0], int(monkeys[monkeys["root"][2]])]
    while current[0] != "humn":
        m1, op, m2 = monkeys[current[0]]
        equals = current[1]

        # If we know m1 and want to know m2
        if isinstance(monkeys[m1], int):
            known = monkeys[m1]

            current[0] = m2
            current[1] = equals - known if op == "+" else known - equals if op == "-" else \
                equals // known if op == "*" else known // equals

        # If we know m2 and want to know m1
        elif isinstance(monkeys[m2], int):
            known = monkeys[m2]

            current[0] = m1
            current[1] = equals - known if op == "+" else equals + known if op == "-" else \
                equals // known if op == "*" else equals * known
    return current[1]


# Tests and Solution ---
print("Tests:")
print(solution_day21_prob2(test01))
print("\nSolution:")
print(solution_day21_prob2(puzzle))


# Note: The conditions for current[1] come from solving this equation for m1 and for m2 for op in ["+", "-", "*", "/"]:
# m1 op m2 = known
