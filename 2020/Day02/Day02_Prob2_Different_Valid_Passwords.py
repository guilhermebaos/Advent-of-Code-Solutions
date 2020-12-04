import re

# Puzzle Input
with open('Day02_Input.txt', 'r') as puzzle_input:
    passwords = puzzle_input.read().split('\n')

# Separate the input
processed_passwords = []
for pass_list in passwords:
    processed_passwords += [re.split(r'[- :]', pass_list)]

# See if passwords are valid
valid = 0
for pass_list in processed_passwords:
    password = pass_list[4]
    letter = pass_list[2]
    if (password[int(pass_list[0]) - 1] == letter) != (password[int(pass_list[1]) - 1] == letter):    # != is an XOR operator
        valid += 1

print(valid)
