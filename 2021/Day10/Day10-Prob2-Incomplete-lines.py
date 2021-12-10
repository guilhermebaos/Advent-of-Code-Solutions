# Puzzle Input ----------
with open('Day10-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day10-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

# Main Code ----------
# Pairs off open and closing delimiters
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# Points for the competition
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


# Return the closers needed to complete a line
def check_line(line: str):
    opens = []
    for item in line:
        # Save the opening character
        if item in pairs.keys():
            opens += [item]

        # Eliminate the opening character or find a corruption in this line
        if item in pairs.values():
            if item == pairs[opens[-1]]:
                opens.pop()
            else:
                return False

    # Reverse the list to get the closers we need in the right order
    opens.reverse()
    return [pairs[item] for item in opens]


# Count the points of a line
def points_line(closers: list):
    global points
    this_points = 0

    # Calculate the points according to the rules
    for item in closers:
        this_points *= 5
        this_points += points[item]
    return this_points


def find_corrupted_lines(data: list):
    # Discard corrupted lines and get the closers needed to complete incomplete lines
    data = list(map(check_line, data))
    total_points = []

    # Get the pitons for each line
    for item in data:
        if item:
            total_points += [points_line(item)]

    # Sort the points and return the middle one
    total_points.sort()
    return total_points[int((len(total_points) - 1) / 2)]


# Tests and Solution ----------
print(find_corrupted_lines(test01))
print(find_corrupted_lines(puzzle))
