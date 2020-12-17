# Puzzle Input
with open('Day17_Test.txt') as puzzle_input:
    flat_region = list(map(list, puzzle_input.read().split('\n')))

# Minimum, Maximum, and number of possible values for x, y, z and w
x_range = [0, len(flat_region[0]), len(flat_region[0]) - 0]
y_range = [0, len(flat_region), len(flat_region) - 0]
z_range = [0, 0, 0]
w_range = [0, 0, 0]

# Map cubes onto 4 1D lists, instead of 1 3D list
cubes_state = []        # Each cube states
cubes_neigh = []        # Each cube neighbors
cubes_coord = []        # Each cube coordinates
index = 0               # Current Index
z, w = 0, 0             # Current starting z and w
for y, row in enumerate(flat_region):       # For every row:
    for x, position in enumerate(row):          # For every position in the row:
        if position == '#':                     # Add the cube's state to the states list
            cubes_state += [1]
        else:
            cubes_state += [0]

        # Calculate the cube's neighbors
        cubes_neigh += [[]]
        for neigh_index, cube in enumerate(cubes_coord):        # For every other cube:
            delta_x = abs(cube[0] - x)                              # Calculate the deltas
            delta_y = abs(cube[1] - y)
            if delta_x < 2 and delta_y < 2:                         # If the deltas are all 0 or 1:
                cubes_neigh[-1] += [neigh_index]                        # The other cube is a neighbor of this one
                cubes_neigh[neigh_index] += [index]                     # This cube is a neighbor of the other one
        cubes_coord += [[x, y, z, w]]                              # Add this cube to the coordinates list
        index += 1                                              # Next cube's index


# Compute the 6 cycles
max_index = index - 1                                           # Index of the next cube
for cycle in range(6):
    zero_layer = 0
    negative_layers = 0
    # Create a list with 0s to hold the next cubes' states
    new_cubes_states = [0 for _ in range((x_range[2] + 3) * (y_range[2] + 3) * (z_range[2] + 3) * (w_range[2] + 3))]
    for w in range(w_range[0] - 1, w_range[1] + 2):             # For every w-coord:
        for z in range(z_range[0] - 1, z_range[1] + 2):             # For every z-coord:
            for y in range(y_range[0] - 1, y_range[1] + 2):             # For every y-coord:
                for x in range(x_range[0] - 1, x_range[1] + 2):             # For every x-coord:
                    try:                                        # If the cube already existed
                        index = cubes_coord.index([x, y, z, w])        # Get it's index

                        # Number of active neighbors
                        active_neigh = 0
                        for neigh in cubes_neigh[index]:            # For every neighbor:
                            try:                                        # If the neighbor existed in the previous cycle:
                                neigh_state = cubes_state[neigh]            # Get it's state
                            except IndexError:                          # If the neighbor is brand new:
                                neigh_state = 0                             # Ignore it
                            active_neigh += neigh_state
                            if active_neigh > 3:                    # Doesn't matter if has more than 3 active neighbors
                                break
                        state = cubes_state[index]                  # Get this cube's state
                        if state == 1 and 2 <= active_neigh <= 3:       # Rules to stay on
                            new_cubes_states[index] = 1
                            if w == 0 and z == 0:
                                zero_layer += 1
                            else:
                                negative_layers += 1
                        elif state == 0 and active_neigh == 3:          # Rules to turn on from off state
                            new_cubes_states[index] = 1
                            if w == 0 and z == 0:
                                zero_layer += 1
                            else:
                                negative_layers += 1
                    except ValueError:                          # If the cube is new
                        index = max_index + 1                       # Get it's new index
                        max_index += 1

                        # Calculate the new cube's neighbors (see above)
                        cubes_neigh += [[]]
                        for neigh_index, cube in enumerate(cubes_coord):
                            delta_x = abs(cube[0] - x)
                            delta_y = abs(cube[1] - y)
                            delta_z = abs(cube[2] - z)
                            delta_w = abs(cube[3] - w)
                            if delta_x < 2 and delta_y < 2 and delta_z < 2 and delta_w < 2:
                                cubes_neigh[-1] += [neigh_index]
                                cubes_neigh[neigh_index] += [index]

                        # Number of active neighbors (see above)
                        active_neigh = 0
                        for neigh in cubes_neigh[index]:
                            try:
                                neigh_state = cubes_state[neigh]
                            except IndexError:
                                neigh_state = 0
                            active_neigh += neigh_state
                            if active_neigh > 3:
                                break
                        if active_neigh == 3:
                            new_cubes_states[index] = 1
                            if w == 0 and z == 0:
                                zero_layer += 1
                            else:
                                negative_layers += 1
                        cubes_coord += [[x, y, z, w]]                  # Add the new cube's coordinates to the list
    print(f'End of Cycle {cycle + 1}')
    print(zero_layer, negative_layers)
    cubes_state = new_cubes_states[:]                           # Change the old states into the new states

    # Update the area to calculate
    for index, state in enumerate(cubes_state):
        if state == 1:
            x = cubes_coord[index][0]
            y = cubes_coord[index][1]
            z = cubes_coord[index][2]
            w = cubes_coord[index][3]
            if x < x_range[0]:
                x_range[0] = x - 1
            elif x > x_range[1]:
                x_range[1] = x + 1
            if y < y_range[0]:
                y_range[0] = y - 1
            elif y > y_range[1]:
                y_range[1] = y + 1
            if z < z_range[0]:
                z_range[0] = z - 1
            elif z > z_range[1]:
                z_range[1] = z + 1
            if w < w_range[0]:
                w_range[0] = w - 1
            elif w > w_range[1]:
                w_range[1] = w + 1
    # Use those values to calculate new ranges for the 3 dimensions
    x_range[2] = x_range[1] - x_range[0]
    y_range[2] = y_range[1] - y_range[0]
    z_range[2] = z_range[1] - z_range[0]
    w_range[2] = w_range[1] - w_range[0]

# Show the number of active cubes
print(zero_layer + 2 * negative_layers)
print(zero_layer, negative_layers)
