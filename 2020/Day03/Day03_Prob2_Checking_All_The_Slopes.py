# Puzzle Input
with open('Day03_Input.txt', 'r') as puzzle_input:
    map_trees = puzzle_input.read().split('\n')

right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

# Test all possible slopes
trees = []
for r, d in zip(right, down):
    # Count trees in the path taken
    x_coor = -r
    trees += [0]
    for y_line, line in enumerate(map_trees):
        if y_line % d == 0:             # Skip some lines
            x_coor += r
            x_coor %= len(line)         # The pattern repeats to the right
            if line[x_coor] == '#':
                trees[-1] += 1

# Calculate the total number os trees
total_trees = trees[0]
for t in trees[1:]:
    total_trees *= t

print(total_trees)
