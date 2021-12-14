# Puzzle Input ----------
with open('Day14-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day14-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------


# Parse the rules into a dictionary
def parse_rules(rules: list):
    new_rules = dict()
    for item in rules:
        key, value = item.split(' -> ')
        new_rules[key] = value
    return new_rules


# Apply the rules to the current polymer
def apply_rules(polymer: list, rules: dict):
    index = 0

    # Execute the rules for each pair of letters
    while index < len(polymer):
        substring = ''.join(polymer[index: index + 2])
        to_insert = rules.get(substring)
        if to_insert:
            polymer.insert(index + 1, to_insert)
            index += 1
        index += 1
    return polymer


# Find the end polymer and return the difference between the most and least common elements
def polymerization(data: list, steps=10):
    # Get the initial polymer and rules
    polymer, rules = list(data[0]), data[2:]
    rules = parse_rules(rules)

    # Apply the rules
    for d in range(steps):
        polymer = apply_rules(polymer, rules)

    # Return the difference in occurrences between the most and least common letters
    unique_letters = list(set(polymer))
    frequency_letters = [polymer.count(let) for let in unique_letters]
    return max(frequency_letters) - min(frequency_letters)


# Tests and Solution ----------
print(polymerization(test01))
print(polymerization(puzzle))
