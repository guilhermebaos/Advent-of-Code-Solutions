import os

parent = r"C:\Users\Gui\Documents\GitHub\Advent-of-Code-Solutions\2022"

for n in range(1, 26):
    name = f"Day{n}"
    path = os.path.join(parent, name)

    # Create Directories
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Directory {name} already exists!")

    # Create Files
    with open(fr"{name}\{name}-Input.txt", "w"):
        pass

    with open(fr"{name}\{name}-Test01.txt", "w"):
        pass

    with open(fr"{name}\{name}-Prob1.py", "w") as file:
        file.write(f"""# Solution for Problem 1 Day {n} of AoC 2022!

# Puzzle Input ----------
with open('{name}-Input.txt', 'r') as file:
    puzzle = file.read().split("\\n")

with open('{name}-Test01.txt', 'r') as file:
    test01 = file.read().split("\\n")


# Code ------------------
def solution_day{n}_prob1(puzzle_in: list):
    return


# Tests and Solution ---
print("Tests:")
print(solution_day{n}_prob1(test01))
print("\\nSolution:")
print(solution_day{n}_prob1(puzzle))
""")

    with open(fr"{name}\{name}-Prob2.py", "w") as file:
        file.write(f"""# Solution for Problem 2 Day {n} of AoC 2022!

# Puzzle Input ----------
with open('{name}-Input.txt', 'r') as file:
    puzzle = file.read().split("\\n")

with open('{name}-Test01.txt', 'r') as file:
    test01 = file.read().split("\\n")


# Code ------------------
def solution_day{n}_prob2(puzzle_in: list):
    return


# Tests and Solution ---
print("Tests:")
print(solution_day{n}_prob2(test01))
print("\\nSolution:")
print(solution_day{n}_prob2(puzzle))
""")
