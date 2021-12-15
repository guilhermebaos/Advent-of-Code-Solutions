from collections import defaultdict

# Puzzle Input ----------
with open('Day15-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day15-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

# Main Code ----------

# Memorize the lowest risk routes to this points
memory = defaultdict(lambda: float('inf'))

# Possible movements
movements = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# Check if a step is valid
def is_valid(next_step: tuple, end: tuple):

    # If it's out of bounds, it's not valid
    if next_step[0] < 0 or next_step[1] < 0:
        return False

    # If it's after the end, it's not valid
    if next_step[0] > end[0] or next_step[1] > end[1]:
        return False
    return True


# Recursively test every path
def recursive_pathing(cavern_map: list, start: tuple, end: tuple, current_path: set, current_risk: int):
    global memory, movements

    # If we can get here faster by another route, abandon this path
    if current_risk >= memory[start]:
        return

    # If we can't get to the end fast enough, abandon this path
    if current_risk + abs(start[0] - end[0]) + abs(start[1] - end[1]) > memory[end]:
        return

    # This is the shortest path here, save it
    memory[start] = current_risk
    if start == end:
        return

    # Try every step from here
    for delta in movements:
        next_step = (start[0] + delta[0], start[1] + delta[1])

        # If we have already been in next_step or it isn't valid, skip it
        if next_step in current_path:
            continue
        if not is_valid(next_step, end):
            continue

        # Recursively search the next step
        next_step_risk = cavern_map[next_step[1]][next_step[0]]
        recursive_pathing(cavern_map, next_step, end, current_path | set(next_step), current_risk + next_step_risk)


# Find the lowest risk path
def lowest_risk_path(data: list):
    global memory

    # Reset the memory for the different inputs
    memory = defaultdict(lambda: float('inf'))

    # Parse the cavern
    cavern_map = list(map(lambda x: list(map(int, x)), data))
    cavern_size = len(cavern_map)

    # Get the star and end tiles
    start = (0, 0)
    end = (cavern_size - 1, cavern_size - 1)

    # Maximum risk for the end point
    memory[end] = 9 * 2 * (cavern_size - 1)

    # Find and return the lowest risk path
    recursive_pathing(cavern_map, start, end, set(), 0)
    return memory[end]


# Tests and Solution ----------
print(lowest_risk_path(test01))
print(lowest_risk_path(puzzle))
