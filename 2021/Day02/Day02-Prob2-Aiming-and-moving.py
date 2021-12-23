# Puzzle Input ----------
with open('Day02-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day02-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Split the command and number into a tuple and convert to the right data type
def split_and_convert(command):
    command = command.split()
    return command[0], int(command[1])


# Find where the submarine goes
def find_position(commands):
    commands = list(map(split_and_convert, commands))

    # Add to the horizontal position, depth and aim
    hor, dep, aim = 0, 0, 0
    for c in commands:
        if c[0] == 'forward':
            hor += c[1]
            dep += c[1] * aim
        elif c[0] == 'down':
            aim += c[1]
        else:
            aim -= c[1]
    return hor * dep


# Tests and Solution ----------
print(find_position(test01))
print(find_position(puzzle))
