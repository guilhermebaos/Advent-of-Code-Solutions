# Puzzle Input
with open('Day10_Input.txt') as puzzle_input:
    joltage_adaptors = puzzle_input.read().split('\n')

# Convert to int
joltage_adaptors = list(map(int, joltage_adaptors))

# The the power outlet (0 Jolts) and device adaptor (max + 3 Jolts)
joltage_adaptors += [0, max(joltage_adaptors) + 3]

# Sort the list
joltage_adaptors.sort()

diff = []
# See the differences
for index in range(len(joltage_adaptors) - 1):
    diff += [joltage_adaptors[index + 1] - joltage_adaptors[index]]

# Print the Result
print(diff.count(1) * diff.count(3))
