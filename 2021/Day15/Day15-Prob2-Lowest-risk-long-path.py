# Puzzle Input ----------
with open('Day15-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day15-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

# Main Code ----------

# Memorize the lowest risk routes to this points
memory = dict()

# Memorize the risk associated with a tile
memory_risks = dict()


# Risk of a cell in the repeating map
def risk_in_cell(cavern_map: list, cavern_size_part: int, cell: tuple):
    global memory_risks

    # If we have previously calculated the risk of a cell, return it
    if cell in memory_risks:
        return memory_risks[cell]

    # The added risk
    x = cell[0] // cavern_size_part
    y = cell[1] // cavern_size_part

    # The loop around to the range 1-9
    risk = cavern_map[cell[1] % cavern_size_part][cell[0] % cavern_size_part] + x + y
    if risk % 9 == 0:
        risk = 9
    else:
        risk %= 9

    # Memorize the risk and return it
    memory_risks[cell] = risk
    return risk


# Get all nearby cells of a given cell
def nearby_cells(cell: tuple, cavern_size: int):
    nearby = list()

    # Right
    if cell[0] + 1 < cavern_size:
        nearby += [(cell[0] + 1, cell[1])]

    # Down
    if cell[1] + 1 < cavern_size:
        nearby += [(cell[0], cell[1] + 1)]

    # Left
    if cell[0] - 1 >= 0:
        nearby += [(cell[0] - 1, cell[1])]

    # Up
    if cell[1] - 1 >= 0:
        nearby += [(cell[0], cell[1] - 1)]

    return nearby


# Iteratively find the lowest risk path associated with every point
# We do this for a cell X by:
#   - Finding a path to all of X's nearby cells
#   - Saying the lowest risk path to X is the risk of X plus the minimum risk of X's nearby cells
#   - If X's risk is lower than one of its nearby cells, check that cell to see if it has a new smallest risk
def iterative_pathing(cavern_map: list, cavern_size_part: int, cavern_size_total: int):
    global memory, memory_risks

    check_now = {(0, 1), (1, 0)}

    # While there are things to check
    while len(check_now) > 0:
        check_next = set()
        for cell in check_now:

            # Check the risks of the nearby cell
            nearby = nearby_cells(cell, cavern_size_total)
            risks = [memory.get(p, float('inf')) for p in nearby]

            # Minimum risk for a given cell
            # It's the minimum risk for the paths to its neighbors plus its own risk
            mini_risk = min(risks) + risk_in_cell(cavern_map, cavern_size_part, cell)
            memory[cell] = mini_risk

            # If one of the nearby children can have a new lowest risk, test it
            for child in nearby:
                if memory.get(child, float('inf')) > mini_risk + risk_in_cell(cavern_map, cavern_size_part, child):
                    check_next.add(child)

        check_now = check_next.copy()


# Find the lowest risk path
def lowest_risk_path(data: list):
    global memory, memory_risks

    # Reset the memory for the different inputs
    memory = dict()
    memory_risks = dict()
    memory[(0, 0)] = 0

    # Parse the cavern
    cavern_map = list(map(lambda x: list(map(int, x)), data))
    cavern_size_part = len(cavern_map)
    cavern_size_total = cavern_size_part * 5

    # Find and return the lowest risk path
    iterative_pathing(cavern_map, cavern_size_part, cavern_size_total)
    return memory[(cavern_size_total - 1, cavern_size_total - 1)]


# Tests and Solution ----------
print(lowest_risk_path(test01))
print(lowest_risk_path(puzzle))
