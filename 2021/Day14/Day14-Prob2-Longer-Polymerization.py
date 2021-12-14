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


# Parse the polymer into frequencies of two-letter pairs
def parse_polymer(polymer: list):
    new_polymer = dict()

    # Save the polymer has a dictionary of the letter pairs in it
    for index in range(len(polymer) - 1):
        substring = ''.join(polymer[index: index + 2])
        new_polymer[substring] = new_polymer.get(substring, 0) + 1
    return new_polymer


# Apply the rules to the current polymer
def apply_rules(polymer: dict, rules: dict, frequencies: dict):
    new_polymer = polymer.copy()

    # See if each of the polymers pairs has a rule applied to it
    for key in polymer:
        new_letter = rules.get(key)

        # Add a new letter between the pair
        if new_letter:

            # Break the pair
            broken_pairs = polymer.get(key)
            new_polymer[key] -= broken_pairs

            # Create two new pairs
            start, end = key[0] + new_letter, new_letter + key[1]
            new_polymer[start] = new_polymer.get(start, 0) + broken_pairs
            new_polymer[end] = new_polymer.get(end, 0) + broken_pairs

            # Add the new letters to the frequencies dict
            frequencies[new_letter] = frequencies.get(new_letter, 0) + broken_pairs

    return new_polymer, frequencies


# Find the end polymer and return the difference between the most and least common elements
def polymerization(data: list, steps=40):
    # Get the initial polymer and rules
    polymer, rules = list(data[0]), data[2:]
    rules = parse_rules(rules)

    # Create the frequencies dictionary
    frequencies = dict()
    for letter in polymer:
        frequencies[letter] = frequencies.get(letter, 0) + 1

    # Parse the polymer into a dictionary
    polymer = parse_polymer(polymer)

    # Apply the rules
    for d in range(steps):
        polymer, frequencies = apply_rules(polymer, rules, frequencies)

    # Return the difference in occurrences between the most and least common letters
    return max(frequencies.values()) - min(frequencies.values())


# Tests and Solution ----------
print(polymerization(test01))
print(polymerization(puzzle))
