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
    while x_speed >= 0 and x <= max_x:
        x += x_speed
        x_pos += [x]
        x_speed -= 1
    x_pos = x_pos[:-1]
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

    # Get all possible initial speeds, by testing all x_speed, y_speed pairs
    all_speeds = 0
    for y_speed in range(-max_y_speed, max_y_speed + 1):
        for x_speed in possible_x_speeds:

            # See if there is a step in the probe's trajectory that's inside the target
            x_steps, y_steps = shoot(target, x_speed, y_speed)
            if x_steps and y_steps:

                # Pad the x_steps to make sure there are at least as many x_steps as there are y_steps
                len_x_steps = len(x_steps)
                len_y_steps = len(y_steps)
                if len_x_steps < len_y_steps and abs(x_steps[-2] - x_steps[-1]) in [0, 1]:
                    x_steps += [x_steps[-1] for _ in range(len_y_steps - len_x_steps)]

                # Try to find a moment where the probe is inside the target
                for index_x, x in enumerate(x_steps):
                    try:
                        if min_x <= x <= max_x and min_y <= y_steps[index_x] <= max_y:
                            all_speeds += 1
                            break
                    except IndexError:
                        break

    return all_speeds


# Tests and Solution ----------
print(shoot_in_style(test01))
print(shoot_in_style(puzzle))
