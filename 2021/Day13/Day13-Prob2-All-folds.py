# Puzzle Input ----------
with open('Day13-Input.txt', 'r') as file:
    puzzle = file.read()

with open('Day13-Test01.txt', 'r') as file:
    test01 = file.read()


# Main Code ----------

# Parse the points and the instructions
def parse_data(points_and_instructions: str):
    # Split the points and the instructions
    points, instructions = points_and_instructions.split('\n\n')

    # Split each points and each instruction
    points = points.split('\n')
    instructions = instructions.split('\n')

    # Convert the points to integers
    points = list(map(lambda x: tuple(map(int, x.split(','))), points))

    # Convert the instructions to a list with a letter and an integer
    instructions = list(map(lambda x: x.split()[-1].split('='), instructions))
    instructions = list(map(lambda x: [x[0], int(x[1])], instructions))

    return points, instructions


# Do a fold
def do_a_fold(points: list, instruction: list):
    orientation, coord = instruction

    # Fold by a vertical line
    if orientation == 'x':
        points = list(map(lambda x: (x[0] if x[0] < coord else -x[0] + 2 * coord, x[1]), points))

    # Fold by a horizontal line
    else:
        points = list(map(lambda x: (x[0], x[1] if x[1] < coord else -x[1] + 2 * coord), points))

    return points


# Print the end result
def print_points(points: list, max_x):
    result = []
    y = 0
    new_points = True

    # While there are points in this y coord
    while new_points:
        new_points = False
        string = ["." for _ in range(max_x)]

        # Add points in this y coord to the current line
        for p in points:
            if p[1] == y:
                new_points = True
                string[p[0]] = '#'

        result += [''.join(string)]
        y += 1

    return result


# Do the first fold
def do_one_fold(points_and_instructions: str):
    points, instructions = parse_data(points_and_instructions)

    # Fold according to each instruction
    min_x = 1e10
    for i in instructions:
        if i[0] == 'x' and i[1] < min_x:
            min_x = i[1]
        points = list(set(do_a_fold(points, i)))

    # Print out the result
    printable = print_points(points, min_x)
    print('\n'.join(printable))


# Tests and Solution ----------
do_one_fold(test01)
do_one_fold(puzzle)
