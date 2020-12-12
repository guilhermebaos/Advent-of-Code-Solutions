# Puzzle Input
with open('Day12_Input.txt') as puzzle_input:
    movement_list = puzzle_input.read().split('\n')

# Calculate the path
facing = 1                          # Way it's facing, 0 -> North,  1 -> East,  2 -> West,  3 -> South
coordinates = [0, 0]                # Coordinates where X-axis is facing North and Y-axis is facing East
for movement in movement_list:
    action = movement[0]            # Get the action
    value = int(movement[1:])       # Get it's value
    if action == 'N':               # Execute the action, by adding or subtracting the value from the boat's current
        coordinates[0] += value     # coordinates
    elif action == 'S':
        coordinates[0] -= value
    elif action == 'E':
        coordinates[1] += value
    elif action == 'W':
        coordinates[1] -= value
    elif action == 'L':             # Turn the boat -> 90º is a change of 1 in it's direction
        facing -= value // 90
    elif action == 'R':
        facing += value // 90
    elif action == 'F':             # Go in the way it's facing
        direction = facing % 4
        if direction == 0:
            coordinates[0] += value
        elif direction == 1:
            coordinates[1] += value
        elif direction == 2:
            coordinates[0] -= value
        elif direction == 3:
            coordinates[1] -= value

# The answer is the sum of the absolute value of the coordinates, because we started at 0, 0
print(sum(list(map(abs, coordinates))))
