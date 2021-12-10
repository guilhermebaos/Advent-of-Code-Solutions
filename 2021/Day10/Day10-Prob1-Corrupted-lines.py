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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


# Check if a line is corrupted, and return it's score
def check_line(line: str):
    opens = []
    for item in line:
        if item in pairs.keys():
            opens += [item]
        if item in pairs.values():
            if item == pairs[opens[-1]]:
                opens.pop()
            else:
                return points[item]
    return 0


def find_corrupted_lines(data: list):
    return sum(list(map(check_line, data)))


# Tests and Solution ----------
print(find_corrupted_lines(test01))
print(find_corrupted_lines(puzzle))
