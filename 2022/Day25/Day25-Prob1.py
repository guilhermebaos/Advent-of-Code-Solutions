# Solution for Problem 1 Day 25 of AoC 2022!

# Puzzle Input ----------
with open('Day25-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day25-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------
digits = {
    "TEMP": ["j", 2],
    "SNAFU": ["=", "-", "0", "1", "2"],
    "DEC": [-2, -1, 0, 1, 2]
}


# Convert a character to an integer between -2 and 2
def char_to_int(char: str) -> int:
    return digits["DEC"][digits["SNAFU"].index(char)]


# Convert an integer between -2 and 2 to a character
def int_to_char(ints: int) -> str:
    return digits["SNAFU"][digits["DEC"].index(ints)]


# Convert SNAFU to decimal
def snafu_to_dec(num_snafu: str) -> int:
    num_dec = 0
    num_snafu = list(num_snafu)
    num_snafu = num_snafu.__reversed__()
    for index, item in enumerate(list(num_snafu)):
        num_dec += 5 ** index * char_to_int(item)
    return num_dec


# Convert decimal to SNAFU
def dec_to_snafu(num_dec: int) -> str:
    base5 = []
    while num_dec > 0:
        base5 += [num_dec % 5]
        num_dec //= 5
    base5 += [0]

    num_snafu = []
    for index, item in enumerate(base5):
        if item < 3:
            num_snafu += [str(item)]
        elif item == 3:
            num_snafu += ["="]
            base5[index + 1] += 1
        elif item == 4:
            num_snafu += ["-"]
            base5[index + 1] += 1
        elif item == 5:
            num_snafu += ["0"]
            base5[index + 1] += 1
    if num_snafu[-1] == "0":
        num_snafu.pop()

    return "".join(list(num_snafu.__reversed__()))


def solution_day25_prob1(puzzle_in: list):
    total = 0
    for item in puzzle_in:
        dec = snafu_to_dec(item)
        total += dec
        print(f"{item:<20} | {dec:>15}")
    print(f"{dec_to_snafu(total):<20} | {total:>15}")
    return dec_to_snafu(sum(list(map(lambda x: snafu_to_dec(x), puzzle_in))))


# Tests and Solution ---
print("Tests:")
print(solution_day25_prob1(test01))
print("\nSolution:")
print(solution_day25_prob1(puzzle))

# 2-=2==-===2=022=10 is wrong