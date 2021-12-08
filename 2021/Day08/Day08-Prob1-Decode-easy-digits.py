# Puzzle Input ----------
with open('Day08-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day08-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Parse each display info
def parse_display(display: str):
    info, readout = display.split(' | ')
    return [info.split(), readout.split()]


# Count how many times 1, 4, 7 and 8 appear
def count_easy_digits(displays: list):
    # Parse the displays
    displays = list(map(parse_display, displays))

    # Get all individual readouts
    readouts_list = [x[1] for x in displays]
    readouts = []
    for item in readouts_list:
        readouts += [x for x in item]

    # Count how many times appear unique-len strings
    readouts_len = list(map(len, readouts))
    return readouts_len.count(2) + readouts_len.count(3) + readouts_len.count(4) + readouts_len.count(7)


# Tests and Solution ----------
print(count_easy_digits(test01))
print(count_easy_digits(puzzle))
