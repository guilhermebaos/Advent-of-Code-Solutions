import re

# Puzzle_input
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
    if int(pass_list[0]) <= password.count(pass_list[2]) <= int(pass_list[1]):
        valid += 1

print(valid)
