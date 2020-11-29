from math import gcd


def compare(n1, n2):
    if n1 > n2:
        return -1
    elif n1 == n2:
        return 0
    else:
        return 1


def simulate(steps, p=(), v=()):
    for step in range(0, steps):
        for index0, body1 in enumerate(p):

            # Calculate velocities
            for body2 in p:
                if body1 == body2:
                    pass
                else:
                    v[index0] += compare(body1, body2)

        for index0, body1 in enumerate(p):

            # Calculate positions
            p[index0] += v[index0]

    return p, v


def lcm(*num):
    len_num = len(num)
    num = list(num)
    if str(type(num[0])) == "<class 'list'>":
        num = num[0]
        len_num = len(num)
    if len_num < 2:
        return None
    elif len_num == 2:
        a = num[0]
        b = num[1]
        if a == b:
            return a
        elif a > b:
            big = a
            small = b
        else:
            big = b
            small = a
        return int(big / gcd(big, small) * small)
    else:
        num[0] = lcm(num[0], num[-1])
        num.pop(-1)
        return lcm(num)


puzzle_positions = [[-16, 15, -9], [-14, 5, 4], [2, 0, 6], [-3, 18, 9]]

test1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
test2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

inputs = puzzle_positions[:]

# Initial value for position, velocity and acceleration
positions = [[0] * len(inputs)] + [[0] * len(inputs)] + [[0] * len(inputs)]
velocities = [[0] * len(inputs)] + [[0] * len(inputs)] + [[0] * len(inputs)]

for index, item in enumerate(inputs):
    positions[0][index] = item[0]
    positions[1][index] = item[1]
    positions[2][index] = item[2]

states_x = [positions[0][:] + velocities[0][:]]
states_y = [positions[1][:] + velocities[1][:]]
states_z = [positions[2][:] + velocities[2][:]]

state_x = c_x = 0
state_y = c_y = 0
state_z = c_z = 0

while True:
    if states_x.__contains__(state_x):
        break
    else:
        c_x += 1
        positions[0], velocities[0] = simulate(1, positions[0], velocities[0])
        state_x = positions[0][:] + velocities[0][:]
print('Done X!')

while True:
    if states_y.__contains__(state_y):
        break
    else:
        c_y += 1
        positions[1], velocities[1] = simulate(1, positions[1], velocities[1])
        state_y = positions[1][:] + velocities[1][:]
print('Done Y!')

while True:
    if states_z.__contains__(state_z):

        break
    else:
        c_z += 1
        positions[2], velocities[2] = simulate(1, positions[2], velocities[2])
        state_z = positions[2][:] + velocities[2][:]
print('Done Z!')

print(c_x, c_y, c_z)
print(lcm(c_x, c_y, c_z))
