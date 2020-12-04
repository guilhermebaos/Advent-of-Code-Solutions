import re

# Puzzle Input
with open('Day04_Input.txt', 'r') as puzzle_input:
    passports = puzzle_input.read().split('\n\n')

fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']

# See fields in alphabetic order
# fields.sort()
# print(fields)


def validate(values):
    # Analise the values

    # byr, Birth Year must be between 1920 and 2002
    if not 1920 <= int(values[0]) <= 2002:
        return False

    # ecl, Eye Color must be in the list
    if not ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].__contains__(values[1]):
        return False

    # eyr, Expiration Year must be between 2020 and 2030
    if not 2020 <= int(values[2]) <= 2030:
        return False

    # hcl, Hair Color is a # followed by exactly six characters 0-9 or a-f
    if not re.match(r'^#[0-9a-f]{6}$', values[3]):
        return False

    # hgt, Height must be in certain intervals according to units
    if values[4].__contains__('cm'):
        if not 150 <= int(values[4][:-2]) <= 193:
            return False
    elif values[4].__contains__('in'):
        if not 59 <= int(values[4][:-2]) <= 76:
            return False
    else:
        return False

    # iyr, Issue Year must be between 2010 and 2020
    if not 2010 <= int(values[5]) <= 2020:
        return False

    # pid, Passport ID is a nine-digit number, including leading zeroes
    if not re.match(r'^[0-9]{9}$', values[6]):
        return False

    return True


# Get the number of valid passports
valid = 0
for pa in passports:
    num_fields = 0
    # Check if the passport has the 7 mandatory fields
    for fi in fields[:-1]:
        if pa.__contains__(fi):
            num_fields += 1
    if num_fields == 7:
        # Separate the values for the fields
        separated = re.split('[ \n]', pa)
        separated.sort()
        if separated[1].__contains__('cid:'):
            separated.pop(1)
        for index, fi in enumerate(separated):
            separated[index] = fi[4:]

        if validate(separated):
            valid += 1

print(valid)
