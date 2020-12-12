# Puzzle Input
with open('Day12_Input.txt') as puzzle_input:
    movement_list = puzzle_input.read().split('\n')

# Calculate the path
boat = [0, 0]
waypoint = [1, 10]
for movement in movement_list:
    action = movement[0]            # Get the action
    value = int(movement[1:])       # Get it's value
    if action == 'N':               # Execute the action, by adding or subtracting the value from thewaypoints current
        waypoint[0] += value        # coordinates, which are relative to the boat
    elif action == 'S':
        waypoint[0] -= value
    elif action == 'E':
        waypoint[1] += value
    elif action == 'W':
        waypoint[1] -= value
    elif action == 'L':                                 # Rotate the waypoint left, it's x value becomes the symmetric
        for _ in range(value // 90):                    # of it's old y value and it's y value becomes it's old x value
            waypoint = [waypoint[1], -waypoint[0]]
    elif action == 'R':                                 # Rotate the waypoint right, it's y value becomes the symmetric
        for _ in range(value // 90):                    # of it's old x value and it's x value becomes it's old y value
            waypoint = [-waypoint[1], waypoint[0]]
    elif action == 'F':                                 # Move the boat to the waypoint {value} number of times
        boat[0] += waypoint[0] * value
        boat[1] += waypoint[1] * value

# The answer is the sum of the absolute value of the coordinates, because we started at 0, 0
print(sum(list(map(abs, boat))))
