# Puzzle Input ----------
with open('Day07-Input.txt', 'r') as file:
    puzzle = list(map(int, file.read().split(',')))

with open('Day07-Test01.txt', 'r') as file:
    test01 = list(map(int, file.read().split(',')))


# Main Code ----------

# How much fuel a crab consumes to get to a certain position
def fuel_to_position(crab, end_pos):
    return abs(crab - end_pos)


# Minimum fuel to get all crabs to the same position
def min_fuel(crab_positions):
    average_pos = sum(crab_positions) / len(crab_positions)

    # How much fuel is spent to get to each position
    fuel_per_position = []
    for pos in range(int(average_pos) + 1):
        fuel_per_position += [sum(list(map(fuel_to_position, crab_positions, [pos for _ in crab_positions])))]

    return min(fuel_per_position)


# Tests and Solution ----------
print(min_fuel(test01))
print(min_fuel(puzzle))
