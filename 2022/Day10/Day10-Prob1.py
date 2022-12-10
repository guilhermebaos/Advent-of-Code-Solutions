# Solution for Problem 1 Day 10 of AoC 2022!

# Puzzle Input ----------
with open('Day10-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day10-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------
interesting = [20 + 40 * x for x in range(6)]
register = 1
cycle = 1


# See if the signal is interesting
def interesting_signal() -> int:
    global interesting, register, cycle
    return cycle * register if cycle in interesting else 0


# Run a tick
def tick(cmd: list) -> int:
    global interesting, register, cycle

    # Execute the command and add the interesting signals to the total
    signal_strength = 0
    if cmd[0] == "noop":
        cycle += 1
    else:
        cycle += 1
        signal_strength += interesting_signal()
        cycle += 1
        register += int(cmd[1])
    signal_strength += interesting_signal()
    return signal_strength


def solution_day10_prob1(puzzle_in: list):
    global register, cycle
    register = 1
    cycle = 1

    # Execute all the commands
    signal_strength = 0
    for move in puzzle_in:
        move = move.split(" ")
        signal_strength += tick(move)
    return signal_strength


# Tests and Solution ---
print("Tests:")
print(solution_day10_prob1(test01))
print("\nSolution:")
print(solution_day10_prob1(puzzle))
