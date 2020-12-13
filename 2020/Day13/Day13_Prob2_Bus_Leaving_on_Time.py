from math import gcd


def lcm(*num):
    num = list(num)
    if str(type(num[0])) == "<class 'list'>":
        num = num[0]
    len_num = len(num)
    if len_num < 2:
        return None
    elif len_num == 2:
        a = num[0]
        b = num[1]
        return int(a * b / gcd(a, b))
    else:
        num[0] = lcm(num[0], num[-1])
        num.pop(-1)
        return lcm(num)


# Puzzle Input
with open('Day13_Input.txt') as puzzle_input:
    bus_info = puzzle_input.read().split('\n')

# Get the departure time and the IDs
bus_id = bus_info[1].split(',')

# Get the indexes for the buses, they have to leave in timestamp t such that: t + index = k * ID, where k is a integer
delta_t = []
for index, ID in enumerate(bus_id):
    if ID != 'x':
        delta_t += [index]

# Remove the x's
while 'x' in bus_id:
    bus_id.remove('x')

# Convert the IDs to integers
bus_id = list(map(int, bus_id))

# Find the timestamp that satisfies all the requirements
time_add = bus_id[0]
timestamp = 0
for index, ID in enumerate(bus_id[1:]):
    while (timestamp + delta_t[index + 1]) % ID != 0:   # While the timestamp doesn't work for the next bus:
        timestamp += time_add       # Add to the timestamp a value that will mantain the solution for the previous buses
    time_add = lcm(time_add, ID)    # That value must be a multiple of the IDs of the buses for which we have solutions,
                                    # because that way we keep the solution: t + index = k * ID, where k is a integer
print(timestamp)                    # (because time_add is a multiple of all solved IDs)
