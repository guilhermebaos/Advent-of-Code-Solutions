from copy import deepcopy

# Puzzle Input ----------
with open('Day25-Input.txt') as file:
    puzzle = file.read().split('\n')
with open('Day25-Test01.txt') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Parse sea cucumbers into a list
def parse_sea_cucumbers(sea_cucumbers: list):
    sea_cucumbers_pos = {'S': [], 'E': []}
    for y, item in enumerate(sea_cucumbers):
        for x, pixel in enumerate(item):
            if pixel == '>':
                sea_cucumbers_pos['E'] += [(x, y)]
            elif pixel == 'v':
                sea_cucumbers_pos['S'] += [(x, y)]
    return sea_cucumbers_pos


# Print sea cucumbers
def print_sea_cucumbers(sea_cucumbers: dict, dim_x: int, dim_y):
    sea_map = [['.' for _ in range(dim_x)] for _ in range(dim_y)]
    for line in sea_map:
        print(''.join(line))
    for x, y in sea_cucumbers['S']:
        sea_map[y][x] = 'v'
    for x, y in sea_cucumbers['E']:
        sea_map[y][x] = '>'
    for line in sea_map:
        print(''.join(line))


# Do a step
def step_cucumbers(sea_cucumbers: dict, dim_x: int, dim_y):
    new_sea_cucumbers = {'S': [], 'E': []}
    moved = False

    # See what East sea cucumbers can move
    all_cucumbers = set(sea_cucumbers['E'] + sea_cucumbers['S'])
    for x, y in sea_cucumbers['E']:
        if ((x + 1) % dim_x, y) not in all_cucumbers:
            new_sea_cucumbers['E'] += [((x + 1) % dim_x, y)]
            moved = True
        else:
            new_sea_cucumbers['E'] += [(x, y)]

    # See what South sea cucumbers can move
    all_cucumbers = set(new_sea_cucumbers['E'] + sea_cucumbers['S'])
    for x, y in sea_cucumbers['S']:
        if (x, (y + 1) % dim_y) not in all_cucumbers:
            new_sea_cucumbers['S'] += [(x, (y + 1) % dim_y)]
            moved = True
        else:
            new_sea_cucumbers['S'] += [(x, y)]

    return new_sea_cucumbers, moved


# Calculate the number of steps until the sea cucumbers stop moving
def steps_until_stop(sea_cucumbers: list):
    dim_y = len(sea_cucumbers)
    dim_x = len(sea_cucumbers[0])
    sea_cucumbers = parse_sea_cucumbers(sea_cucumbers)
    steps = 0
    while True:
        sea_cucumbers, moved = step_cucumbers(sea_cucumbers, dim_x, dim_y)
        steps += 1
        if not moved:
            return steps


# Tests and Solution ----------
print(steps_until_stop(test01))
print(steps_until_stop(puzzle))
