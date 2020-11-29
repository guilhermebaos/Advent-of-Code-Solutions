def compare(n1, n2):
    if n1 > n2:
        return -1
    elif n1 == n2:
        return 0
    else:
        return 1


puzzle_positions = [[-16, 15, -9], [-14, 5, 4], [2, 0, 6], [-3, 18, 9]]

test1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
test2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

# Initial value for position, velocity and acceleration
positions = test1[:]
velocities = []

for item in positions:
    velocities += [[0, 0, 0]]

num_coords = len(positions[0])

for step in range(0, 20):
    print(f'\nStep {step + 1}:')
    for index, body1 in enumerate(positions):

        # Calculate velocities
        for body2 in positions:
            if body1 == body2:
                pass
            else:
                for coor in range(0, num_coords):
                    velocities[index][coor] += compare(body1[coor], body2[coor])

    for index, body1 in enumerate(positions):

        # Calculate positions
        for coor in range(0, num_coords):
            positions[index][coor] += velocities[index][coor]

    for index, item in enumerate(zip(positions, velocities)):
        print(f'Body {index + 1}: Pos: {item[0]}, Vel:{item[1]}')

# Calculate each moon's energy
Pot_ene = []
Kin_ene = []
for item in positions:
    Pot_ene += [0]
    Kin_ene += [0]
for index, item in enumerate(zip(positions, velocities)):
    for coor in item[0]:
        Pot_ene[index] += abs(coor)
    for coor in item[1]:
        Kin_ene[index] += abs(coor)
print(Pot_ene, Kin_ene)
# Calculate System's energy
Total = 0
for item in zip(Pot_ene, Kin_ene):
    Total += item[0] * item[1]
print(f'\nTotal Energy in the System: {Total}')
