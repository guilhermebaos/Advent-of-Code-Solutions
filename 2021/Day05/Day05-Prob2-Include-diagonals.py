# Puzzle Input ----------
with open('Day05-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day05-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

# Main Code ----------

# The map of the ocean bed
vent_map = dict()


# Make the vents a tuple with integers
def parse_vent(line: str):
    start, end = line.split(' -> ')
    return tuple(tuple(map(int, point.split(','))) for point in [start, end])


# Returns the points which are part of a vent
def points_in_vent(line: tuple):
    global vent_map
    start, end = line

    # Vertical Vents
    if start[0] == end[0]:
        min_y, max_y = min(start[1], end[1]), max(start[1], end[1])
        for y in range(min_y, max_y + 1):
            p = (start[0], y)
            vent_map[p] = vent_map.get(p, 0) + 1

    # Horizontal Vents
    elif start[1] == end[1]:
        min_x, max_x = min(start[0], end[0]), max(start[0], end[0])
        for x in range(min_x, max_x + 1):
            p = (x, start[1])
            vent_map[p] = vent_map.get(p, 0) + 1

    # Diagonal Vents
    else:
        # We start by finding out the smaller x and then find if for increasing x the y increases or decreases
        if start[0] < end[0]:
            start_x, end_x = start[0], end[0] + 1
            start_y, end_y = start[1], end[1]
        else:
            start_x, end_x = end[0], start[0] + 1
            start_y, end_y = end[1], start[1]

        direction = 1 if end_y > start_y else -1
        end_y += direction

        # Generate the points
        for x, y in zip(range(start_x, end_x), range(start_y, end_y, direction)):
            p = (x, y)
            vent_map[p] = vent_map.get(p, 0) + 1


# Find the places where two or more vents overlap
def find_overlaps(lines_list: list):
    global vent_map
    vent_map = dict()

    # Parse and filter the vents
    parsed_vents = list(map(parse_vent, lines_list))

    # Add the vents' points to the sea floor bed
    for line in parsed_vents:
        points_in_vent(line)

    # Count the overlaps
    overlaps = 0
    for num in vent_map.values():
        overlaps += num > 1
    return overlaps


# Tests and Solution ----------
print(find_overlaps(test01))
print(find_overlaps(puzzle))
