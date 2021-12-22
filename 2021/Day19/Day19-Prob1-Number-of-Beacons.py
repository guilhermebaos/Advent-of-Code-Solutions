# Puzzle Input ----------
with open('Day19-Input.txt', 'r') as file:
    puzzle = file.read().split('\n\n')

with open('Day19-Test01.txt', 'r') as file:
    test01 = file.read().split('\n\n')


# Main Code ----------

# Note to self: Don't forget to reset global variables!

# Parse the raw data into a tuple of tuples, one for each beacon for each scanner
def parse_data(scanner_data: str):
    scanner_data = scanner_data.split('\n')[1:]
    scanner_data = tuple(map(
        lambda x: tuple(map(int, x.split(','))),
        scanner_data
    ))
    return scanner_data


# Vectors drawn starting at each beacon and ending at another beacon, for every scanner
def draw_vectors(data: list):
    vectors = []
    for scanner in data:
        vectors += [[]]
        for index1, beacon1 in enumerate(scanner):
            vectors[-1] += [[]]
            for index2, beacon2 in enumerate(scanner):
                vectors[-1][-1] += [tuple(b2 - b1 for b1, b2 in zip(beacon1, beacon2))]
    return vectors


# Possible orientations of scanners in relation to scanner 0
def possible_orientations():
    orientations = set()
    for x in ['x', '-x']:
        for y in ['y', '-y']:
            for z in ['z', '-z']:
                orientations.add((x, y, z))
                orientations.add((z, x, y))
                orientations.add((y, z, x))
    return orientations


# Change the orientation of a vector
def change_orientation(vector: tuple, orientation: tuple):
    x, y, z = vector
    new_vector = [0, 0, 0]
    for index, item in enumerate(orientation):
        if item == 'x':
            new_vector[index] = x
        elif item == '-x':
            new_vector[index] = -x
        elif item == 'y':
            new_vector[index] = y
        elif item == '-y':
            new_vector[index] = -y
        elif item == 'z':
            new_vector[index] = z
        elif item == '-z':
            new_vector[index] = -z
    return tuple(new_vector)


# Compare two scanners, one if the absolute scanner, the other is the comparison one
def compare_scanners(abs_vectors: list, other_vectors: list):
    orientations = possible_orientations()
    for abs_beacon in abs_vectors:
        for other_beacon in other_vectors:
            for orient in orientations:

                matches = 0
                for other_vec in other_beacon:
                    if other_vec == (0, 0, 0):
                        matches += 1
                        continue

                    changed_vector = change_orientation(other_vec, orient)
                    if changed_vector in abs_beacon:
                        matches += 1

                    if matches == 12:
                        return abs_beacon, other_beacon, orient
    return False, False, False


# Match beacons in different scanners
def match_beacons(data: list, vectors: list):
    abs_beacons = list(data.pop(0))
    abs_vectors = list(vectors.pop(0))

    for other_vectors in vectors:
        abs_beacon, other_beacon, orient = compare_scanners(abs_vectors, other_vectors)
        if not abs_beacon:
            continue
        abs_beacon_index = abs_beacon.index((0, 0, 0))
        print(abs_beacon_index)


# Find the number of beacons in range of scanners
def number_of_beacons(data: list):
    data = list(map(parse_data, data))
    vectors = draw_vectors(data)
    match_beacons(data, vectors)


# Tests and Solution ----------
print(number_of_beacons(test01))
# print(number_of_beacons(puzzle))
