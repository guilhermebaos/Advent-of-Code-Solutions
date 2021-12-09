# Puzzle Input ----------
with open('Day09-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day09-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

# Main Code ----------

# Checked points and the ones we found to be low points
checked = set()
low_points = []


# Convert to integer
def parse_data(row: str):
    return [int(x) for x in row]


# Check all nearby points to a point
def check_nearby_points(data: list, item: int, y: int, x: int, max_y: int, max_x: int):
    global checked, low_points

    if y > 0:
        if item >= data[y - 1][x]:
            checked.update([(y, x)])
            return
        else:
            checked.update([(y - 1, x)])

    if y < max_y:
        if item >= data[y + 1][x]:
            checked.update([item])
            return
        else:
            checked.update([(y + 1, x)])

    if x > 0:
        if item >= data[y][x - 1]:
            checked.update([item])
            return
        else:
            checked.update([(y, x - 1)])

    if x < max_x:
        if item >= data[y][x + 1]:
            checked.update([item])
            return
        else:
            checked.update([(y, x + 1)])

    low_points += [(y, x)]


# Recursively find all points in this basin
def check_this_basin(data: list, y: int, x: int, max_y: int, max_x: int):
    basin = [(y, x)]
    point_queue = [(y, x)]

    # Use BFS to find all points of a basin
    while len(point_queue) > 0:
        y, x = point_queue.pop()
        if y > 0 and data[y - 1][x] != 9 and (y - 1, x) not in basin:
            basin += [(y - 1, x)]
            point_queue += [(y - 1, x)]

        if y < max_y and data[y + 1][x] != 9 and (y + 1, x) not in basin:
            basin += [(y + 1, x)]
            point_queue += [(y + 1, x)]

        if x > 0 and data[y][x - 1] != 9 and (y, x - 1) not in basin:
            basin += [(y, x - 1)]
            point_queue += [(y, x - 1)]

        if x < max_x and data[y][x + 1] != 9 and (y, x + 1) not in basin:
            basin += [(y, x + 1)]
            point_queue += [(y, x + 1)]

    return len(basin)


# Check all points nearby from this one point
def find_basins(data: list):
    global checked, low_points
    checked = set()
    low_points = []

    # Parse the data into integers
    data = list(map(parse_data, data))

    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    # Search every point in our map
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if (y, x) not in checked:
                check_nearby_points(data, item, y, x, max_y, max_x)

    # Find every basin in our map
    basins = []
    for y, x in low_points:
        basins += [check_this_basin(data, y, x, max_y, max_x)]
    basins.sort(reverse=True)

    return basins[0] * basins[1] * basins[2]


# Tests and Solution ----------
print(find_basins(test01))
print(find_basins(puzzle))
