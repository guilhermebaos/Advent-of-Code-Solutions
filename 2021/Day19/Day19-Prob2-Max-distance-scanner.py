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


# Possible orientations of scanners in relation to scanner 0
def possible_orientations():
    orientations = set()
    for x in ['x', '-x']:
        for y in ['y', '-y']:
            for z in ['z', '-z']:
                orientations.add((x, y, z))
                orientations.add((y, x, z))
                orientations.add((z, x, y))
                orientations.add((x, z, y))
                orientations.add((y, z, x))
                orientations.add((z, y, x))
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


# Try every orientation for a scanners beacons and try to fit them to another scanners' beacons
def possible_match(abs_beacons, other_beacons):
    all_orientations = possible_orientations()

    # Save the absolute beacons as a set
    set_abs_beacons = set(abs_beacons)
    for end in abs_beacons:
        for orientation in all_orientations:

            # Try changing the orientation of the coordinates of all other beacons
            new_other_beacons = [change_orientation(other_b, orientation) for other_b in other_beacons]

            # Try considering each beacon a possible match and make it coincide with the end beacon
            for start in new_other_beacons:
                translation = [end[i] - start[i] for i in range(3)]

                # Translate all other beacons by the same vector
                translated_beacons = tuple(
                    tuple(new_other_b[i] + translation[i] for i in range(3)) for new_other_b in new_other_beacons)

                # If there are enough matches, return the translation vector!
                if len(set(translated_beacons) & set_abs_beacons) >= 12:
                    return translated_beacons, translation
    return False, False


# Find the number of beacons in range of scanners
def size_of_ocean(data: list):
    data = list(map(parse_data, data))

    # Save all beacons and all scanners found so far
    all_beacons = set(data[0])
    all_scanners = {(0, 0, 0)}

    # Do a search for all scanners and try to see if they overlap with another scanner, starting at scanner 0
    check_next = [data.pop(0)]
    while len(check_next) > 0:
        check_now = check_next.copy()
        check_next = []

        # Try to match these two scanners
        for abs_beacon in check_now:
            for other_beacon in data[:]:
                new_beacons, translation = possible_match(abs_beacon, other_beacon)

                # Save the new beacons and add the scanner to be searched next
                if new_beacons:
                    # It takes a couple minutes
                    print('Match!')
                    all_beacons.update(set(new_beacons))

                    # The translation vector is the absolute positions of the scanner!
                    all_scanners.add(tuple(translation))

                    check_next += [new_beacons]
                    data.remove(other_beacon)

    # Return the maximum distance between two scanners
    return max(sum(abs(scanner1[i] - scanner2[i]) for i in range(3)) for scanner1 in all_scanners for scanner2 in all_scanners)


# Tests and Solution ----------
print(size_of_ocean(test01))
print('\n\n')
print(size_of_ocean(puzzle))
