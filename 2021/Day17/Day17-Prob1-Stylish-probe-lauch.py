# Puzzle Input ----------
puzzle = [(60, 94), (-171, -136)]

test01 = [(20, 30), (-10, -5)]

# Main Code ----------

# Save the patterns for x and y positions, with an initial velocity
pos_x = dict()
pos_y = dict()


# Get the x positions given a initial speed (> 0)
def x_positions(x_speed: int, min_x: int, max_x: int):
    x = 0
    x_pos = [x]

    # Add the speed and reduce it by 1, until 0
    while x_speed > 0 and x <= max_x:
        x += x_speed
        x_pos += [x]
        x_speed -= 1
    return x_pos if min_x <= x_pos[-1] <= max_x else False


# Get the y position given a initial speed (> 0)
def y_positions(y_speed: int, min_y: int, max_y: int):
    y = 0
    y_pos = [y]

    # Add the speed and reduce it by 1
    while y >= min_y:
        y += y_speed
        y_pos += [y]
        y_speed -= 1
    y_pos = y_pos[:-1]
    return y_pos if min_y <= y_pos[-1] <= max_y else False


# Shoot a probe
def shoot(target: list, x_speed: int, y_speed: int):
    global pos_x, pos_y

    # Get the extremes of the target rectangle
    min_x, max_x, min_y, max_y = target[0] + target[1]

    # Use the saved positions if we have them, otherwise calculate it
    if x_speed in pos_x:
        x_steps = pos_x[x_speed]
    else:
        x_steps = x_positions(x_speed, min_x, max_x)
        pos_x[x_speed] = x_steps

    # Use the saved positions if we have them, otherwise calculate it
    if y_speed in pos_y:
        y_steps = pos_y[y_speed]
    else:
        y_steps = y_positions(y_speed, min_y, max_y)
        pos_y[y_speed] = y_steps

    return x_steps, y_steps


# Highest height reached by the probe
def shoot_in_style(target: list):
    global pos_x, pos_y
    pos_x = dict()
    pos_y = dict()

    # Get the extremes of the target rectangle
    min_x, max_x, min_y, max_y = target[0] + target[1]

    # Using the sum of arithmetic progression to find out minimum x speed to hit target
    min_x_speed = int((2 * min_x) ** 0.5)
    max_x_speed = max_x + 1

    # The speed coming down and passing through 0  is symmetric to the speed going up
    max_y_speed = abs(min_y)

    # All possible x speeds
    possible_x_speeds = list(range(min_x_speed, max_x_speed))

    # Get the maximum height, by testing all x_speed, y_speed pairs
    max_height = 0
    for y_speed in range(max_y_speed):
        for x_speed in possible_x_speeds:

            # See if it's possible that this shot landed in the target
            x_steps, y_steps = shoot(target, x_speed, y_speed)
            if x_steps and y_steps:
                max_height = max(y_steps + [max_height])

        y_speed += 1

    return max_height


# Tests and Solution ----------
print(shoot_in_style(test01))
print(shoot_in_style(puzzle))
