# Puzzle_input
with open('Day03_Input.txt', 'r') as puzzle_input:
    map_trees = puzzle_input.read().split('\n')

# Count trees in the path taken
x_coor = -3
trees = 0
for line in map_trees:
    x_coor += 3
    x_coor %= len(line)         # The pattern repeats to the right
    if line[x_coor] == '#':
        trees += 1

print(trees)
