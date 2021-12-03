# Puzzle Input ----------
with open('Day03-Input.txt', 'r') as file:
    puzzle = list(map(list, file.read().split('\n')))

with open('Day03-Test01.txt', 'r') as file:
    test01 = list(map(list, file.read().split('\n')))


# Main Code ----------
def most_common_bits(diagnostic, index_to_check):
    # Size of binary numbers
    len_num = len(diagnostic[0])
    len_dgc = len(diagnostic)

    # Get the number of ones that appear in each position
    frequency_of_ones = 0
    for num in diagnostic:
        frequency_of_ones += int(num[index_to_check])

    # Get the most (and least) common bits in each position
    most_common = '1' if frequency_of_ones >= len_dgc / 2 else '0'
    return most_common


def find_oxygen(diagnostic):
    index = 0
    while len(diagnostic) > 1:
        most_common = most_common_bits(diagnostic, index)

        # Only the numbers with the most common bit in this position can be the oxygen number
        new_diagnostic = []
        for num in diagnostic[:]:
            if num[index] == most_common:
                new_diagnostic += [num]

        diagnostic = new_diagnostic[:]
        index += 1

    return int(''.join(diagnostic[0]), 2)


def find_carbon(diagnostic):
    index = 0
    while len(diagnostic) > 1:
        most_common = most_common_bits(diagnostic, index)
        # Only the numbers with the least common bit in this position can be the oxygen number
        new_diagnostic = []
        for num in diagnostic[:]:
            if num[index] != most_common:
                new_diagnostic += [num]

        diagnostic = new_diagnostic[:]
        index += 1

    return int(''.join(diagnostic[0]), 2)


def life_support_rating(diagnostic):
    return find_oxygen(diagnostic) * find_carbon(diagnostic)


# Tests and Solution ----------
print(life_support_rating(test01))
print(life_support_rating(puzzle))
