# Solution for Problem 2 Day 10 of AoC 2022!

# Puzzle Input ----------
with open('Day10-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day10-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------
screen = [["" for _ in range(40)] for _ in range(6)]
register = 1
cycle = 1


# Draw the image with the cathode ray tube
def crt():
    global register, cycle, screen
    if cycle > 240:
        return

    # Draw a pixel on screen
    y, x = (cycle-1) // 40, (cycle - 1) % 40
    screen[y][x] = "#" if abs(register - x) < 2 else "."


# Run a tick
def tick(cmd: list):
    global register, cycle

    # Execute the command
    if cmd[0] == "noop":
        cycle += 1
    else:
        cycle += 1
        crt()
        cycle += 1
        register += int(cmd[1])

    # Draw a pixel
    crt()
    return


def solution_day10_prob2(puzzle_in: list):
    global register, cycle, screen
    screen = [["" for _ in range(40)] for _ in range(6)]
    register = 1
    cycle = 1
    crt()

    # Execute all the commands
    for move in puzzle_in:
        move = move.split(" ")
        tick(move)
    for line in screen:
        print(''.join(line))
    return


# Tests and Solution ---
print("Tests:")
print(solution_day10_prob2(test01))
print("\nSolution:")
print(solution_day10_prob2(puzzle))
