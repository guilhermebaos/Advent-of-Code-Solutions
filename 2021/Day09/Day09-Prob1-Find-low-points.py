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

    low_points += [item]


# Check all points nearby from this one point
def find_low_points(data: list):
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

    return sum(low_points) + len(low_points)


# Tests and Solution ----------
print(find_low_points(test01))
print(find_low_points(puzzle))
