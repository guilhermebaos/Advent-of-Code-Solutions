# Puzzle Input ----------
with open('Day02-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day02-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Split the command and number into a tuple and convert to the right data type
def split_and_convert(commands):
    new_commands = []
    for c in commands:
        c = c.split()

        # Convert the second part of the command to an integer
        new_commands += [(c[0], int(c[1]))]
    return new_commands


# Find where the submarine goes
def find_position(commands):
    commands = split_and_convert(commands)

    # Add to it's horizontal position or depth
    hor, dep = 0, 0
    for c in commands:
        if c[0] == 'forward':
            hor += c[1]
        elif c[0] == 'down':
            dep += c[1]
        else:
            dep -= c[1]
    return hor * dep


# Tests and Solution ----------
print(find_position(test01))
print(find_position(puzzle))
