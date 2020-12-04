# Puzzle Input
with open('Day04_Input.txt', 'r') as puzzle_input:
    passports = puzzle_input.read().split('\n\n')

fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']

# Get the number of valid passports
valid = 0
for pa in passports:
    num_fields = 0
    # Check if the passport has the 7 mandatory fields
    for fi in fields[:-1]:
        if pa.__contains__(fi):
            num_fields += 1
    if num_fields == 7:
        valid += 1

print(valid)
